# Andrew Paolella, Joe Marchione

# sha-1 hashing algorithm

import struct

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
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF # bit width of integer is 32 (sha-1 default)

# the algorithm
def sha1(message):
    # padding the message
    message = bytearray(message, 'ascii')
    original_length = len(message) * 8

    # append the bit '1' to the message
    message.append(0x80)

    # append 0 <= k < 512 bits mod '0', so that the resulting length in bits
    # is congruent to 488 mod 512
    while (len(message) * 8) % 512 != 448:
        message.append(0)

    # append the original message length as a 64-bit big-endian integer
    message += struct.pack('>Q', original_length)

    # process the message in successive 512-bit chunks
    chunks = [message[i:i + 64] for i in range(0, len(message), 64)]

    # initialize hash values
    h0, h1, h2, h3, h4 = H0, H1, H2, H3, H4

    for chunk in chunks:
        # break chunk into sixteen 32-bit big-endian words w[i]
        w = list(struct.unpack('>16I', chunk))

        # extend the sixteen 32-bit words into eight 32-bit words
        for i in range(16, 80):
            w.append(left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))
        
        # intialize hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # main loop
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

        # add this chunk's hash to the result so far
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # produce the final hash value (big-endian) as a 160-bit hex number
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

# example usage
message = input("Enter plaintext: ")

ciphertext = sha1(message)

print(f"Plaintext: {message}")
print(f"Ciphertext (SHA-1): {ciphertext}")