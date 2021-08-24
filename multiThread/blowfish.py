# Blowfish based encryptography system

from os import access, pipe, sendfile, system
from Crypto.Cipher import Blowfish
from Crypto import Random
from rich.console import Console
import time
import base64

console = Console()

def encrypt_message(msg):
    key = Random.new().read(16)
    block_size = Blowfish.block_size
    iv = Random.new().read(Blowfish.block_size)
    padding = "*"
    def p(s): return s+(block_size - len(s) % block_size)*padding
    c = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    Ecp_msg = iv + c.encrypt(p(msg).encode('ascii'))
    return [key, base64.b64encode(Ecp_msg)]

def decrypt_message(key, Ecp_msg):
    block_size = Blowfish.block_size
    Encrypted_msg = base64.b64decode(Ecp_msg)[block_size:]
    iv = base64.b64decode(Ecp_msg)[:block_size]
    final = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return final.decrypt(Encrypted_msg).decode('ascii').rstrip('*')


def menu(action, msg, Final):
    console.print(" ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗", style='bold red')
    console.print(" ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║", style='bold red')
    console.print(" ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝", style='bold red')
    console.print('                              [i]your encryptation program[/i]\n\n[b]Make a wish[b]')
    console.print('[1] Encrypt\n[2] Decode\n[3] E X I T\n')
    action = input('> ')
    if action == '1':
        console.print('\nGive me a message', style='bold red')
        msg = input('')
        Final = encrypt_message(msg)
        console.print("\nYOUR GENERATED KEY", style='bold yellow')
        print(Final[0])
        console.print("\nENCRYPTED MESSAGE", style='bold yellow')
        print(Final[1])
        time.sleep(3)
    elif action == '2':
        if Final != '':
            console.print("\DECODED MESSAGE", style='bold yellow')
            fim = decrypt_message(Final[0], Final[1])
            print(fim)
            print("\n")
            console.print("[b]Rebooting system...[/b]")
            Final = ''
        else:
            console.print("WRONG!\nPlease don't forget to enter your message!", style='bold red')
            time.sleep(1)
    elif action == '3':
        return
    else:
        console.print('Unexpected number, try again!', style='bold red')
    menu(action, msg, Final)


if __name__ == '__main__':
    action = ''
    msg = ''
    Final = ''
    menu(action, msg, Final)

