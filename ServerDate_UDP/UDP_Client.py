#importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 51000 # porta a se conectar

clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

message = input('Digite o comando: ')

while message != 'data' :
    message = input('Erro, digite o comando novamente: ')

clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor

modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta

print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedMessage.decode('utf-8')))

clientSocket.close() # encerra o socket do cliente
