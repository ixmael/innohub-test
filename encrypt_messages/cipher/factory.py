from .caesar_cipher import CaesarCipher

def get_cipher(cipher_name):
    '''
    TODO: Agregar más funciones de cifrado
    '''
    ciphers_allowed = ['caesar']
    
    if cipher_name in ciphers_allowed:
        if cipher_name == 'caesar':
            return CaesarCipher()
    else:
        raise Exception('The cipher "{}" is not implemented.'.format(cipher_name))
