from socket import *

serverName = ''
serverPort = 12000

#Criando o socket TCP com conexão a internet
clientSocket = socket(AF_INET, SOCK_STREAM)
# vai solicitar acesso ao servidor
clientSocket.connect((serverName,serverPort))

sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode('utf-8')) #enviando o texto para o servidor   
finalSentence = clientSocket.recv(1024)
print ('The Server: (\'%s\', %d)  has answred: %s' % (serverName, serverPort, finalSentence.decode
('utf-8'))) 
clientSocket.close()