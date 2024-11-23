import struct
import secrets 

# constants
H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0

# circular left shift operation rotate integer 'n' by 'b' number of bits
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

# the algorithm
def sha1(message, salt=None):
    # If no salt is provided, generate a random salt (16 bytes)
    if salt is None:
        salt = secrets.token_bytes(16)  # 16 bytes salt

    # Combine message with salt (salt is added in front of the message)
    salted_message = bytearray(salt + message.encode('ascii'))  # Convert to bytearray

    # Padding the salted message
    original_length = len(salted_message) * 8  # Length in bits
    salted_message.append(0x80)  # Add the 1-bit padding

    while (len(salted_message) * 8) % 512 != 448:  # Make length 448 mod 512
        salted_message.append(0)

    # Append the original message length as a 64-bit big-endian integer
    salted_message += struct.pack('>Q', original_length)

    # Prepare to process the message in successive 512-bit chunks
    chunks = [salted_message[i:i + 64] for i in range(0, len(salted_message), 64)]

    # Initialize our five working variable hash values
    h0, h1, h2, h3, h4 = H0, H1, H2, H3, H4

    for chunk in chunks:
        # Break 512-bit chunk into sixteen 32-bit big-endian words w[i]
        w = list(struct.unpack('>16I', chunk))

        # Extend the sixteen 32-bit words into eighty 32-bit words
        for i in range(16, 80):
            w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))
        
        # Initialize five working variable hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main compression function (80 rounds)
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            
            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to the result so far
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Produce the final hash value (big-endian) as a 160-bit hex number
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4), salt.hex()

# Example usage
message = input("Enter plaintext: ")

ciphertext, salt = sha1(message)

print(f"Plaintext: {message}")
print(f"Ciphertext (SHA-1 with Salt): {ciphertext}")
print(f"Salt: {salt}")
