# Blowfish based encryptography system

from os import access, pipe, sendfile, system
from Crypto.Cipher import Blowfish
from Crypto import Random
from rich.console import Console
import time
import base64

console = Console()

def encrypt_message(msg, key):
    block_size = Blowfish.block_size
    iv = Random.new().read(Blowfish.block_size)
    padding = "*"
    def p(s): return s+(block_size - len(s) % block_size)*padding
    c = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    Ecp_msg = iv + c.encrypt(p(msg).encode('utf-8'))    
    return [key, base64.b64encode(Ecp_msg)]

def decrypt_message(key, Ecp_msg):
    block_size = Blowfish.block_size
    Encrypted_msg = base64.b64decode(Ecp_msg)[block_size:]
    iv = base64.b64decode(Ecp_msg)[:block_size]
    final = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return final.decrypt(Encrypted_msg).decode('ascii').rstrip('*')

