from cryptography.fernet import Fernet

def encrypt_message(message, encryption_key):
    f = Fernet(encryption_key)
    encrypted_message = f.encrypt(message.encode())
    print (encrypted_message,"Encrypted message")
    return encrypted_message


# Generate a key (this should be done once and saved for future use)
key = Fernet.generate_key()
print("Generated Key:", key)

# Take user input for the message and the encryption key
message = input("Enter the message to encrypt: ")
encryption_key = input("Enter the encryption key (make sure it's valid): ")

# Make sure the encryption key is in bytes (if entered as a string, convert it to bytes)
encryption_key = encryption_key.encode()

# Encrypt the message
encrypt_message(message, encryption_key)