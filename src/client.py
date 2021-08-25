import socket
import argparse

#vc pode mudar o host e a porta de entrada
parser = argparse.ArgumentParser(description="This is a client for multthreads connections")
parser.add_argument('--host', metavar= 'host', type= str, nargs='?', default= socket.gethostname())
parser.add_argument('--port', metavar= 'port', type= int, nargs='?', default= 13000)
arg = parser.parse_args()

print(f"Connecting to server: {arg.host} on port {arg.port}")
#criando socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((arg.host, arg.port))
    except Exception as e: #caso apareça algum erro
        raise SystemExit(f"We cant connect to {arg.host} on {arg.port} because: {e}")

    while True:
        print('Please enter your message')
        sentence = input("")
        sck.sendall(sentence.encode('utf-8')) #manda mensagem para o servidor
        if sentence == 'exit': #palavra chave de saida do loop
            print('Client is desconnecting....')
            break
        result = sck.recv(1024)
        print(f"Your response from Server is: {result}")
