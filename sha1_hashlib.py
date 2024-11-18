# Joe Marchione , Andrew Paolella

# Example implementation of the SHA-1 cryptographic hash algorithm
#  using the built in hashlib library. 
# We will use this for testing against our own SHA-1 implementation.

import hashlib      #https://docs.python.org/3/library/hashlib.html
#import hmac        #https://docs.python.org/3/library/hmac.html#module-hmac // Can combine cryptographic hash function with a secret key.
import os
#import secrets #https://docs.python.org/3/library/secrets.html used for implementing salt

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
    with open(path, "a") as f:
        f.writelines(f"\nplaintext: {plaintext}")
        f.writelines(f"\nciphertext: {ciphertext}")

        print("Data has been saved successfully.")


plaintext = input("Enter plaintext: ")
ciphertext = hash_plaintext(plaintext)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext (SHA-1): {ciphertext}")

save_file(ciphertext)


'''A hashing algorithm is a complex mathemtical function that transforms input data into an ouput string of fixed length.
The same input string will always produce the same output string. We can not go backwards, only forward with hashing.
Instead of storing an actual password in a database, the actual hash is stored in the DB. We can add a layer of hardening with salting.
Salting are short random set of characters appeneded to a users password before they're hashed. The user wont know a salt is being used.
Salts are generally sotred in plaintxt along with the hash output. Finally, there are peppers. A pepper is a short random string or charaacter.
A pepper is specifically something not stored in the database, pheraabs in the application code or a secure memory enclave.'''