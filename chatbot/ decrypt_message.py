from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, encryption_key):
    f = Fernet(encryption_key=encryption_key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message