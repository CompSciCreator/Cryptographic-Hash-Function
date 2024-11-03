


# Define the super-increasing knapsack (private key)
private_key = [1, 2, 4, 10, 20, 40]

# Choose n and m according to the requirements
n = 31
m = 110

# Step 1: Derive the public key from the private key, n, and m
def derive_public_key(private_key, n, m):
    return [(n * x) % m for x in private_key]

# Calculate public key
public_key = derive_public_key(private_key, n, m)
print("Private key:", private_key)
print("Public key:", public_key)

# Function to convert a plaintext message to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Function to encrypt the binary message using the public key
def knapsack_encrypt(binary_text, public_key):
    # Split the binary message into chunks matching the public key length
    chunks = [binary_text[i:i+len(public_key)] for i in range(0, len(binary_text), len(public_key))]
    ciphertext = []
    for chunk in chunks:
        # Pad chunk if it's shorter than public key
        chunk = chunk.zfill(len(public_key))
        # Calculate the sum based on the public key and binary chunk
        cipher_value = sum(int(bit) * public_key[i] for i, bit in enumerate(chunk))
        ciphertext.append(cipher_value)
    return ciphertext

# Function to decrypt the ciphertext using the private key, n, and m
def knapsack_decrypt(ciphertext, private_key, n, m):
    # Calculate the modular inverse of n modulo m
    modular_inverse_n = pow(n, -1, m)
    binary_message = ""
    for cipher_value in ciphertext:
        # Decrypt each cipher value by multiplying with the modular inverse and taking modulo m
        decrypted_value = (cipher_value * modular_inverse_n) % m
        # Convert the decrypted value back to binary based on the private key
        binary_chunk = []
        for weight in reversed(private_key):
            if decrypted_value >= weight:
                binary_chunk.append('1')
                decrypted_value -= weight
            else:
                binary_chunk.append('0')
        binary_message += ''.join(reversed(binary_chunk))  # Add decrypted chunk to message
    return binary_message

# Example usage:
original_message = "hi"
binary_message = text_to_binary(original_message)

# Encrypt the binary message using the knapsack public key
ciphertext = knapsack_encrypt(binary_message, public_key)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext back to the binary message
decrypted_binary = knapsack_decrypt(ciphertext, private_key, n, m)
print("Decrypted binary:", decrypted_binary)

# Convert binary back to text
decrypted_text = ''.join(chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8))
print("Decrypted text:", decrypted_text)
