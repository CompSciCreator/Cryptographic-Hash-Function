# Joe Marchione , Andrew Paolella

# Example implementation of the SHA-1 cryptographic hash algorithm
#  using the built in hashlib library. 
# We will use this for testing against our own SHA-1 implementation.

import hashlib      #https://docs.python.org/3/library/hashlib.html
#import hmac        #https://docs.python.org/3/library/hmac.html#module-hmac // Can combine cryptographic hash function with a secret key.
import os

def hash_plaintext(plaintext):
    
    # convert plaintext into utf-8 bytes
    plaintext_bytes = plaintext.encode('utf-8')

    # hash the plaintext bytes into a hash object using SHA-1
    hash_object = hashlib.sha1(plaintext_bytes)

    # returns the hash object as a hexadecimal string
    hashed_output = hash_object.hexdigest()

    return hashed_output

# Writing output file to desktop - AP 
def save_file(ciphertext):

    # Get the user's desktop path. os.path.join(): Join one or more path components. os.path.expanduser(): expands initial path component ~ or ~user in given path to user’s home directory. 
    desktop_path = os.path.join(os.path.expanduser("~"), "Documents")  # updated for compatibilty 
        
    # Create the file path
    path = os.path.join(desktop_path, "haslib_output.txt")

    # Write the hash to the file , will be created if doesnt exist 
    with open(path, "w") as f:
        f.write(f"plaintext: {plaintext}")
        f.write(f"\nciphertext: {ciphertext}")

        print("Data has been saved successfully.")


plaintext = input("Enter plaintext: ")
ciphertext = hash_plaintext(plaintext)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext (SHA-1): {ciphertext}")

save_file(ciphertext)