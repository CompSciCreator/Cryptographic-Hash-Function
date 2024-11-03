# Andrew Paolella , (insert names here)
# ! pip install cryptography (python package) 

import os
import base64
from cryptography.fernet import Fernet







class AES:   
    # Class private variables
    SECRET_KEY = "Follow_The_White_Rabbit_Neo"
    SALT = "ssshhhhhhhhhhh!!!!"

    def encrypt(message):
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode('utf-8')
    

    def decrypt(encrypted_message):
        key = Fernet.generate_key()  # Replace with the actual key used for encryption
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message.encode()).decode('utf-8')
    return decrypted_message







    




