# Andrew Paolella , Jessica Kressner (insert names here)
# ! pip install cryptography (python package) 

import os
#import base64
#import numpy as np
import hashlib

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms



#TODO: Incorporate knapsack with AES. Includes generating a super-increasing knapsack (private key), deriving the hard knapsack (public key), and encrypting/decrypting a message with these keys



# Create Constants
SECRET_KEY = b"my_super_secret_key_ho_ho_ho"
SALT = b"ssshhhhhhhhhhh!!!!"
IV = bytes([0] * 16)  # Static IV as in Java code, but note this is not secure for production use

def generate_key(secret_key, salt):
    #TODO Key derivation function similar to Java's PBKDF2WithHmacSHA256

    # Convert the secret key to bytes
    secret_key_bytes = secret_key.encode('utf-8')

    # Define the key derivation function PBKDFWithHmacSHA1
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA1(),
        secret_key = secret_key,
        salt = salt
    )

    # Derive the key
    derived_key = kdf.derive(secret_key_bytes)

    # Return the derived key
    return derived_key

def encrypt(text, secret_key, salt):

    
    try:
        # TODO: Generate the AES key

        # Calls the generate key function
        aes_key = generate_key(secret_key, salt)
        # Prints the generated AES key to the screen
        print(f"Generated aes key: {aes_key}")

        # TODO: Initialize AES cipher in CBC mode with padding
        
        # TODO: Pad text to AES block size
    
        # TODO: Encrypt and encode to base64
    

def decrypt(encrypted_text, secret_key, salt):
    try:
        # TODO: Generate the AES key

        # Calls the generate key function
        aes_key = generate_key(secret_key, salt)
        # Prints the generated AES key to the screen
        print(f"Generated aes key: {aes_key}")
        
        
        # TODO: Initialize AES cipher in CBC mode
 
        
        # TODO: Decode from base64 and decrypt
       
        # TODO: Remove padding
        
# Example usage
if __name__ == "__main__":
    original_string = "hello"
    encrypted_string = encrypt(original_string)
    decrypted_string = decrypt(encrypted_string)

    print("Original:", original_string)
    print("Encrypted:", encrypted_string)
    print("Decrypted:", decrypted_string)
