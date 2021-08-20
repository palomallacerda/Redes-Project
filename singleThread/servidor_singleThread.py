from socket import * #importando todos os metódos dessa biblioteca
import threading 

def server(serverport = 12000, serverName = 'localhost'):
    #metodo socket recebe dois parametros o tipo de socket (no caso da internet, serviço que ele ta 
    # operando ou seja TCP)
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #informa qual  o endereço ip associado e a porta usada pelo servidor
    serverSocket.bind((serverName,serverport))

    #Colocando no modo escuta, deixando-o pronto para aceitar conexões
    serverSocket.listen(1)
    print('This server is ready to receive on %d port'%(serverport))

    while 1:
        # metodo accept cria conecction socket o endereço de memoria do qual a conexão foi estabelecida, ou seja,
        # qual socket do cliente#
        # addr é o endereço ip e a porta de destino
        print('Waiting to receive a client message....')
        connectionSocket, addr = serverSocket.accept()
        #recebe até 1024 caracteres
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode('utf-8')
        #transforma para maiusculo com o UPPER
        capitalizedSentence = sentence.upper()
        print('Client %s has send: %s, changing to: %s' %(addr, sentence, capitalizedSentence))
        #manda de volta a frase convertida
        connectionSocket.send(capitalizedSentence.encode('utf-8'))
        #encerra conexão
        connectionSocket.close()
    
threading.Thread(target=server).start()
