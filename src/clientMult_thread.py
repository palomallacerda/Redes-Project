import socket
import argparse 
import blowfish
from rich.console import Console
import time
import base64
console = Console()

def menu(action, msg, Final,key):
        console.print(" ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗", style='bold red')
        console.print(" ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║", style='bold red')
        console.print(" ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝", style='bold red')
        console.print('                              [i]your encryptation program[/i]\n\n[b]Make a wish[b]')
        console.print('[1] Encrypt\n[2] Decode\n[3] E X I T\n')
        action = input('> ')
        sck.send(action.encode('utf-8'))
        if(action!=3):       
            if action == '1':
                console.print('\nGive me a message', style='bold red')
                msg = input('>> ')
                sck.sendall(msg.encode('utf-8')) #manda mensagem para o servidor  
                console.print('\nGive me a key with minimum 4 caracters', style='bold red')
                key = input('>> ')
                sck.sendall(key.encode('utf-8')) #manda mensagem para o servidor  
                Final = sck.recv(1024) #recebe mensagem encriptada
                console.print("\nENCRYPTED MESSAGE", style='bold yellow')
                print(Final.decode())
                time.sleep(0.5)
                console.print("\nPLEASE WAIT\nRESTARTING SYSTEM....", style='bold yellow')
                time.sleep(2)
            elif action == '2':
                if Final == '': # vai inserir uma mensagem pra decodificar//AINDA N TA FUNCIONANDO
                    console.print('\nGive me a encrypted message', style='bold red')
                    if msg == '':
                        msg = input('>> ')
                        console.print('\nGive me a key with minimum 6 caracters', style='bold red')
                        key = input('>> ')
                        Descrypt = blowfish.decrypt_message(key.encode(), msg)  
                        console.print("\nPLEASE WAIT\nRESTARTING SYSTEM....", style='bold yellow')
                        time.sleep(2)
                        console.print("\nDECODED MESSAGE", style='bold yellow')
                        print(Descrypt)
                else: # vai decodificar a mensagem que já foi inserida anteriormente
                    console.print("\nPLEASE WAIT\nDESCODING MESSAGE....", style='bold yellow')#colocar uns movimentos 
                    time.sleep(2)
                    console.print("\nDECODED MESSAGE", style='bold yellow')
                    Descrypt_msg = sck.recv(1024)
                    print(Descrypt_msg.decode())
                    time.sleep(1)                                    
        if action == '3': 
            console.print("Shutting down System.....", style='bold yellow')
            time.sleep(0.5)
            return True
        menu(action, msg, Final, key)

#vc pode mudar o host e a porta de entrada
parser = argparse.ArgumentParser(description="This is a client for multthreads connections")
parser.add_argument('--host', metavar= 'host', type= str, nargs='?', default= socket.gethostname())
parser.add_argument('--port', metavar= 'port', type= int, nargs='?', default= 14000)
arg = parser.parse_args()
print(f"Connecting to server: {arg.host} on port {arg.port}")
#criando socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((arg.host, arg.port))
    except Exception as e: #caso apareça algum erro
        raise SystemExit(f"We cant connect to {arg.host} on {arg.port} because: {e}")
    
    while True:
        action = ''
        msg = ''
        Final = ''
        key = ''
        shut = menu(action, msg, Final,key)
        if shut == True: break
