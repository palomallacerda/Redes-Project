from os import pipe
from Crypto.Cipher import Blowfish
from Crypto import Random
import base64


## Função que encriptografa
def Encrypt(msg):
    key = Random.new().read(16) #gera uma chave aleatória entre 0 e 16
    block_size = Blowfish.block_size
    iv = Random.new().read(Blowfish.block_size)
    padding = "*"
    p = lambda s: s+(block_size -len(s)% block_size)*padding
    c = Blowfish.new(key,Blowfish.MODE_CBC,iv)
    Ecp_msg = iv+ c.encrypt(p(msg).encode('ascii'))
    return [key, base64.b64encode(Ecp_msg)]


## função que decodifica
def Densencrypt(key, Ecp_msg):
    block_size = Blowfish.block_size
    Encrypted_msg = base64.b64decode(Ecp_msg)[block_size:]
    iv = base64.b64decode(Ecp_msg)[:block_size]
    final = Blowfish.new(key,Blowfish.MODE_CBC,iv)
    return final.decrypt(Encrypted_msg).decode('ascii').rstrip('*')

print('Digite sua mensagem')
msg = input('')
Final = Encrypt(msg)
print(Final[0])
print("Your encrypted message:")
print(Final[1])
print("Your message:")
print(Densencrypt(Final[0], Final[1]))

