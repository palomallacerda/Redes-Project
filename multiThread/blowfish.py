#Sistema de encriptografia usando o método Blowfish

from os import access, pipe, system
from Crypto.Cipher import Blowfish
from Crypto import Random
import base64

## Função que encriptografa
def Encrypt(msg):
    key = Random.new().read(16) #gera uma chave aleatória entre 0 e 16
    block_size = Blowfish.block_size #gera o bloco de encriptação
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

def menu():
    while True:
        print(" ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗")
        print(" ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║")       
        print(" ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝")        
        print('                              your encryptation program\n\nPlease enter your operation')
        print('1-Encrypt\n3-Exit\n')
        action = input('')
        msg = ''
        Final = ''
        if action == '1':
            print('\nPlease enter your message')
            msg = input('')
            Final = Encrypt(msg)
            print("\nYour encrypted message is:")
            print(Final[1])
        elif action == '3':
            break    
        else:  # Arrumar uma forma de fazer o loop
            print("Unexpected input reloading systeam.....\n")
            menu()

        print("\nDo you want to:\n2-Decode\n3-exit\n")
        action = input('')

        if action == '2':
            print("\nYour decoded message:")
            fim = Densencrypt(Final[0], Final[1])
            print(fim)
        if action == '3':
            break

menu()