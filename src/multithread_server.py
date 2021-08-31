import socket
import argparse
import threading
import blowfish

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

def on_new_client(i, client, connection, client_message, key, encrypted_message):
	ip = connection[0]
	port = connection[1]
	if i:
		print(f"A new connection was made from IP: {ip}, and port: {port}!\n")
	action = client.recv(1024).decode('utf-8')

	while True:
		if action == '1':
			client_message = client.recv(1024).decode()
			key = client.recv(1024)
			print(f"The client message is: {client_message}\n and key:{key}\n")
			encrypted_message = blowfish.encrypt_message(client_message, key)
			print(f"We are sending the encrypted message: {encrypted_message[1].decode()}")
			print(f"With key: {encrypted_message[0].decode()}")
			client.sendall(encrypted_message[1])

		if action == '2':
			user_encrypted_message = client.recv(1024)
			user_encrypted_key = client.recv(1024)
			print(f"Decoding the client message: {user_encrypted_message.decode()}\n with key:{user_encrypted_key}\n")
			try:
				return_message = blowfish.decrypt_message(user_encrypted_key, user_encrypted_message.decode())
				print(f"Sending decoded message:{return_message}")
				client.sendall(return_message.encode())
			except Exception as e:
				print(f"We couldn't decode {user_encrypted_message.decode()}, because: {e}")
				client.sendall(' '.encode())

		if action == '3':
			print(f"Client {ip} on port: {port} is saying good-bye")
			break
		on_new_client(0, client, connection, '', '', encrypted_message)

while True:
	try:
		client, ip = sck.accept()
		encrypted_message = ''
		client_message =''
		key = ''
		threading._start_new_thread(on_new_client,(1, client, ip, client_message, key, encrypted_message))
	except KeyboardInterrupt:
		print('\nWe are shutting down the server!')
		break
	except Exception as e:
		print(f"Something went wrong: {e}")
		break
sck.close()