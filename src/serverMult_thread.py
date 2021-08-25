import base64
import socket
import argparse
import threading
import base64
from typing import final 
import blowfish

# blowfish decodificar
parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket demo!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 14000)
args = parser.parse_args()

print(f"Running the server on: {args.host} and port: {args.port}")

sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	sck.bind((args.host, args.port))
	sck.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")
	

def on_new_client(client, connection, msg, key, Final):
	ip = connection[0]
	port = connection[1]
	print(f"A new connection was made from IP: {ip}, and port: {port}!\n Waiting for a message....")
	action = client.recv(1024)
	action = action.decode('utf-8')
	while True:
		if action == '1': 
			msg = client.recv(1024)
			msg = msg.decode()
			key = client.recv(1024)
			print(f"The client message is: {msg}\n and key:{key}\n")
			Final = blowfish.encrypt_message(msg, key)
			print(f"We are sending the encrypted message: {Final[1].decode()}")
			print(f"We are sending the encrypted key: {Final[0]}")
			client.sendall(Final[1])
		if action == '2': #arrumar uma forma de reconhecer quando for decodificar uma mensagem já inserida ou n
			print(f"Decoding the client message: {msg}\n with key:{key}\n")
			Final = blowfish.encrypt_message(msg, key)
			Final_des = blowfish.decrypt_message(Final[0],Final[1])
			print(f"Sending decoded message:{Final_des}")
			client.sendall(Final_des.encode())
		if action == '3':
			return
		on_new_client(client, connection, msg, key, Final)
				
while True:
	try: 
		client, ip = sck.accept()
		Final = ''
		msg =''
		key = ''
		threading._start_new_thread(on_new_client,(client, ip,msg, key, Final))
	except KeyboardInterrupt:
		print('We are shutting down the server!')
		break
	except Exception as e:
		print(f"Something went wrong: {e}")
sck.close()