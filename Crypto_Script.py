import os
import base64
import hashlib

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Constants
SECRET_KEY = b"my_super_secret_key_ho_ho_ho"
SALT = b"ssshhhhhhhhhhh!!!!"
IV = os.urandom(16)  # random IV changed from static

def generate_key(secret_key, salt):
    # Key derivation 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), #for the time being using sha256, we can change it if we want
        length=32,  # sha256 is 32-byte key
        salt=salt,
        iterations=100000  
    )

    # Derive the key
    derived_key = kdf.derive(secret_key)
    return derived_key

def encrypt(text, secret_key, salt):
    try:
        # Generate the AES key
        aes_key = generate_key(secret_key, salt)

        # Generate a random IV
        iv = os.urandom(16)

        # Initialize AES cipher in CBC mode with the random IV
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        # Pad text to AES block size
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()

        # Encrypt and encode to base64
        encrypted = encryptor.update(padded_data) + encryptor.finalize()

        # Combine IV and encrypted data and encode to base64
        encrypted_iv_and_data = base64.b64encode(iv + encrypted).decode('utf-8')
        return encrypted_iv_and_data

    except Exception as e:
        print(f"Error during encryption: {e}")


def decrypt(encrypted_text, secret_key, salt):
    try:
        # Generate the AES key
        aes_key = generate_key(secret_key, salt)

        # Decode from base64
        encrypted_data_with_iv = base64.b64decode(encrypted_text)

        # Extract the IV (first 16 bytes) and encrypted data
        iv = encrypted_data_with_iv[:16]
        encrypted_data = encrypted_data_with_iv[16:]

        # Initialize AES cipher in CBC mode with extracted IV
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        # Decrypt and remove padding
        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted.decode('utf-8')

    except Exception as e:
        print(f"Error during decryption: {e}")
        
# Example usage
if __name__ == "__main__":
    original_string = "hello"
    encrypted_string = encrypt(original_string, SECRET_KEY, SALT)
    decrypted_string = decrypt(encrypted_string, SECRET_KEY, SALT)

    print("Original:", original_string)
    print("Encrypted:", encrypted_string)
    print("Decrypted:", decrypted_string)
