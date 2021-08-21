#Sistema de encriptografia usando o método Blowfish

from os import access, pipe, sendfile, system
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


def menu( action, msg, Final):
    print(" ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗")
    print(" ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║")       
    print(" ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝")        
    print('                              your encryptation program\n\nPlease enter your operation')
    print('1-Encrypt\n2-Decode\n3-Exit\n')
    action = input('')
    if(action!=3):       
        if action == '1':
            print('\nPlease enter your message')
            msg = input('')
            Final = Encrypt(msg)
            print("\nYour Generaded key is:")
            print(Final[0]) 
            print("\nYour encrypted message is:")
            print(Final[1])
        elif action == '2':
            if Final != '':
                print("\nYour decoded message:")
                fim = Densencrypt(Final[0], Final[1])
                print(fim)
                print("\n")
                print("Rebooting Systeam......")
                Final = ''
            else:
                print("WRONG!\nPlease don't forget to enter your message!")
        elif action == '3':
            return
        else:
            print('Unexpected number, try again!')
        menu(action, msg, Final)

def main():        
    action = ''
    msg = ''
    Final = ''
    menu(action, msg, Final)

main()
