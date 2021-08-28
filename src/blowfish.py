# Blowfish based encryptography system

from os import access, pipe, sendfile, system
from Crypto.Cipher import Blowfish
from Crypto import Random
from rich.console import Console
import time
import base64

console = Console()

def IsBase64(str):#verifica se a mensagem a ser codificada ta na base certa
    try:
        base64.b64decode(str)
        return True
    except Exception as e:
        return False

def encrypt_message(msg, key): #função para encriptar
    block_size = Blowfish.block_size
    iv = Random.new().read(Blowfish.block_size)
    padding = "*"
    def p(s): return s+(block_size - len(s) % block_size)*padding
    c = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    Ecp_msg = iv + c.encrypt(p(msg).encode('utf-8'))    
    return [key, base64.b64encode(Ecp_msg)]

def decrypt_message(key, Ecp_msg):#função para decodificar
    if IsBase64(Ecp_msg):
        block_size = Blowfish.block_size
        Encrypted_msg = base64.b64decode(Ecp_msg)[block_size:]
        iv = base64.b64decode(Ecp_msg)[:block_size]
        final = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        return final.decrypt(Encrypted_msg).decode('ascii').rstrip('*')
    else:
        return False
    

