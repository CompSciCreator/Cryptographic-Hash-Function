# Andrew Paolella, Joe Marchione

# sha-1 hashing algorithm

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

    return

# example usage
message = input("Enter plaintest: ")

ciphertext = sha1(message)

print(f"Plaintext: {message}")
print(f"Ciphertext (SHA-1): {ciphertext}")