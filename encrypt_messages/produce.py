'''
'''
import os
import sys
from dotenv import load_dotenv
from cipher import get_cipher
from services import get_service

load_dotenv()

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        raise Exception('Necesitas agregar el mensaje que quieres cifrar y publicar')

    cipher = get_cipher(os.getenv("CIPHER_NAME"))
    message_ciphered = cipher.cipher(sys.argv[1])
    service = get_service(os.getenv("SERVICE_NAME"))
    service.post(message_ciphered)
