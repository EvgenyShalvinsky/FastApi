from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    return base64.urlsafe_b64encode(os.urandom(32))

def encrypt_secret(secret: str):
    key = generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(secret.encode())
    return {'key': key.decode(), 'value': encrypted.decode()}

def decrypt_secret(key: str, encrypted_secret: str):
    fernet = Fernet(key.encode())
    return fernet.decrypt(encrypted_secret.encode()).decode()