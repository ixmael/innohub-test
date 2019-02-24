'''
'''
import os
import sys
from dotenv import load_dotenv
from cipher import get_cipher
from services import get_service

load_dotenv()

if __name__ == "__main__":
    service = get_service(os.getenv("SERVICE_NAME"))
    cipher_message = service.read()

    cipher = get_cipher(os.getenv("CIPHER_NAME"))
    message = cipher.decipher(cipher_message)
    print(message)
