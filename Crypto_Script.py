# Andrew Paolella , (insert names here)
# ! pip install cryptography (python package) 

#import os
#import base64
#import numpy as np


    







#TODO: Incorporate knapsack with AES. Includes generating a super-increasing knapsack (private key), deriving the hard knapsack (public key), and encrypting/decrypting a message with these keys























# Create Constants
SECRET_KEY = b"my_super_secret_key_ho_ho_ho"
SALT = b"ssshhhhhhhhhhh!!!!"
IV = bytes([0] * 16)  # Static IV as in Java code, but note this is not secure for production use

def generate_key(secret_key, salt):
    #TODO Key derivation function similar to Java's PBKDF2WithHmacSHA256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=16,  # AES-128
        salt=salt,
        iterations=65536,
        backend=default_backend()
    )
    return kdf.derive(secret_key)

def encrypt(text):
    try:
        # TODO: Generate the AES key
        key = generate_key(SECRET_KEY, SALT)
        
        # TODO: Initialize AES cipher in CBC mode with padding
        cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # TODO: Pad text to AES block size
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()
        
        # TODO: Encrypt and encode to base64
        encrypted = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(encrypted).decode('utf-8')
    except Exception as e:
        print(f"Error while encrypting: {e}")
        return None

def decrypt(encrypted_text):
    try:
        # TODO: Generate the AES key
        key = generate_key(SECRET_KEY, SALT)
        
        # TODO: Initialize AES cipher in CBC mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # TODO: Decode from base64 and decrypt
        encrypted_data = base64.b64decode(encrypted_text)
        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()
        
        # TODO: Remove padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
        
        return decrypted.decode('utf-8')
    except Exception as e:
        print(f"Error while decrypting: {e}")
        return None

# Example usage
if __name__ == "__main__":
    original_string = "hello"
    encrypted_string = encrypt(original_string)
    decrypted_string = decrypt(encrypted_string)

    print("Original:", original_string)
    print("Encrypted:", encrypted_string)
    print("Decrypted:", decrypted_string)
