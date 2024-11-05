#Andrew Paolella 

'''This code uses SHA-256, which provides a 256-bit output and is much more secure than SHA-1, 
especially regarding collision resistance.'''

import hashlib # haslib Documentation: https://docs.python.org/3/library/hashlib.html

# String to hash
Secret_Key = "Follow the white rabbit, Neo."

# Create a SHA-1 hash object
hash_object = hashlib.sha1(Secret_Key.encode())

# Get the hexadecimal representation of the hash    
hex_dig = hash_object.hexdigest()

'''hexdigest is returned as a string object of double length, containing only hexadecimal digits. 
This may be used to exchange the value safely in email or other non-binary environments.'''

# Print hash 
print(hex_dig)