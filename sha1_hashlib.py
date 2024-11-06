# Joe Marchione

# Example implementation of the SHA-1 cryptographic hash algorithm
#  using the built in hashlib library. 
# We will use this for testing against our own SHA-1 implementation.

import hashlib

def hash_plaintext(plaintext):
    
    # convert plaintext into utf-8 bytes
    plaintext_bytes = plaintext.encode('utf-8')

    # hash the plaintext bytes into a hash object using SHA-1
    hash_object = hashlib.sha1(plaintext_bytes)

    # returns the hash object as a hexadecimal string
    hashed_output = hash_object.hexdigest()

    return hashed_output


plaintext = input("Enter plaintext: ")

ciphertext = hash_plaintext(plaintext)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext (SHA-1): {ciphertext}")