# sha-1 hashing algorithm with salting

import struct #Interpret bytes as packed binary data
#https://docs.python.org/3/library/struct.html#module-struct

import secrets #The secrets module is used for generating random numbers for managing important data such as passwords, account authentication, security tokens, and related secrets, that are cryptographically strong. 
#https://docs.python.org/3/library/secrets.html

# constants
H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0

# circular left shift operation rotate integer 'n' by 'b' number of bits
def left_rotate(n, b):
    # (n << b) shifts the integer n left by b bits, any bits that 'fall off' are discarded
    # (n >> (32 - b)) shifts n right by (32 - b) bits, bringing the leftmost bits to the right side
    # a bitwise 'OR' combines the results achieving circular rotation
    # 0xFFFFFFFF masks the result to ensure it fits within 32 bits
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

    # append 0 <= k < 512 bits mod '0', so that the resulting length in bits
    # is congruent to 488 mod 512
    while (len(salted_message) * 8) % 512 != 448:  
        salted_message.append(0)

    # Append the original message length as a 64-bit big-endian integer
    # this completes our padding
    salted_message += struct.pack('>Q', original_length)

    # Prepare to process the message in successive 512-bit chunks
    chunks = [salted_message[i:i + 64] for i in range(0, len(salted_message), 64)]

    # Initialize our five working variable hash values
    h0, h1, h2, h3, h4 = H0, H1, H2, H3, H4

    for chunk in chunks:
        # Break 512-bit chunk into sixteen 32-bit big-endian words w[i]
        w = list(struct.unpack('>16I', chunk))

        # Extend the sixteen 32-bit words into eighty 32-bit words
        # by XORing and rotating bits from previous words

        for i in range(16, 80):
            w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))
        
        # Initialize five working variable hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main compression function (80 rounds)
        # divided into four stages of 20 rounds
        # logical operations are performed on our 5 working variables with
        # 4 different values of k for each round constant
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

            # 'temp' calculates a new value to be used for 'a' in the next iteration
            # by rotating the bits left by 5 and adding other variables to it to
            # ensure non-linearity and diffusion
            
            # 'a' is the most active variable, 'b', 'c', and 'd' are used in logical operations
            # 'e' acts as a passive accumulator to ensure that small changes in the input
            # propegate through all 80 rounds.
            
            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to the result so far
        # the original constant values are added to the iterated working variables
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Produce the final hash value (big-endian) as a 160-bit hex number
    # (our five 32-bit working variables are concatenated together)

    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4), salt.hex()

# Example usage
message = input("Enter plaintext: ")

ciphertext, salt = sha1(message)

print(f"Plaintext: {message}")
print(f"Ciphertext (SHA-1 with Salt): {ciphertext}")
print(f"Salt: {salt}")
