import socket
import argparse
import blowfish
from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def menu(action, user_message, return_message, key):
        console.print(" ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗", style='bold red')
        console.print(" ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║", style='bold red')
        console.print(" ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝", style='bold red')
        console.print('                              [i]your encryptation program[/i]\n\n[b]Make a wish[b]')
        console.print('[1] Encrypt\n[2] Decode\n[3] E X I T\n')
        action = input('> ')
        sck.send(action.encode('utf-8'))

        if action == '1':
            console.print('\nGive me a message', style='bold red')
            user_message = input('>> ')
            sck.sendall(user_message.encode('utf-8'))
            console.print('\nGive me a key with minimum 4 caracters', style='bold red')
            key = input('>> ')
            sck.sendall(key.encode('utf-8'))
            return_message = sck.recv(1024)
            with Progress() as progress:
                        taks_1 = progress.add_task("[yellow]Processing....", total=100)
                        time.sleep(0.3)
                        while not progress.finished:
                            progress.update(taks_1, advance=40)
                            time.sleep(1)
            console.print("\nENCRYPTED MESSAGE", style='bold yellow')
            print(return_message.decode())
            time.sleep(0.5)
            console.print("\nRESTARTING SYSTEM....", style='bold yellow')
            time.sleep(2)

        elif action == '2':
            if return_message == '':
                console.print('\nGive me a encrypted message', style='bold red')
                if user_message == '':
                    user_message = input('>> ')
                    console.print('\nGive me a key with minimum 6 caracters', style='bold red')
                    key = input('>> ')
                    decrypted_message = True
                    with Progress() as progress:
                        taks_1 = progress.add_task("[yellow]Processing....", total=100)
                        time.sleep(0.3)
                        while not progress.finished:
                            progress.update(taks_1, advance=40)
                            time.sleep(1)

                    decrypted_message = blowfish.decrypt_message(key.encode(), user_message)
                    if decrypted_message == False:
                        console.print("\nINVALID MESSAGE, TRY AGAIN....\n", style='bold yellow')
                        time.sleep(0.2)
                    else:
                        console.print("\nPLEASE WAIT\nRESTARTING SYSTEM....", style='bold yellow')
                        time.sleep(3)
                        console.print("\nDECODED MESSAGE", style='bold yellow')
                        print(decrypted_message)
            else:
                console.print("\nPLEASE WAIT\nDECODING PREVIOUS MESSAGE...", style='bold yellow')#colocar uns movimentos
                time.sleep(2)
                with Progress() as progress:
                        taks_1 = progress.add_task("[yellow]Processing....", total=100)
                        time.sleep(0.3)
                        while not progress.finished:
                            progress.update(taks_1, advance=40)
                            time.sleep(1)
                console.print("\nDECODED MESSAGE", style='bold yellow')
                decrypt_user_message = sck.recv(1024)
                print(decrypt_user_message.decode())
                time.sleep(1)

        if action == '3':
            console.print("Shutting down server...", style='bold yellow')
            time.sleep(0.5)
            return True
        menu(action, user_message, return_message, key)


parser = argparse.ArgumentParser(description="This is a client for multthreads connections")
parser.add_argument('--host', metavar= 'host', type= str, nargs='?', default= socket.gethostname())
parser.add_argument('--port', metavar= 'port', type= int, nargs='?', default= 14000)
arg = parser.parse_args()
print(f"Connecting to server: {arg.host} on port {arg.port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((arg.host, arg.port))
    except Exception as e:
        raise SystemExit(f"We cant connect to {arg.host} on {arg.port} because: {e}")

    while True:
        action = ''
        user_message = ''
        return_message = ''
        key = ''
        shut = menu(action, user_message, return_message,key)
        if shut == True: break
