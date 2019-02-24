import os

class CaesarCipher():
    def __init__(self):
        self.key = int(os.getenv("CAESEAR_KEY"))

        self.L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
        self.I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    def cipher(self, plaintext):
        ciphertext = ""
        for c in plaintext.upper():
            if c.isalpha():
                ciphertext += self.I2L[ (self.L2I[c] + self.key)%26 ]
            else:
                ciphertext += c

        return ciphertext
    
    def decipher(self, ciphered_message):
        message = ''
        for c in ciphered_message.upper():
            if c.isalpha():
                message += self.I2L[ (self.L2I[c] - self.key)%26 ]
            else:
                message += c
        
        return message
