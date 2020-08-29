# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula (python 3)
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = input('Digite o comando: ')

while sentence != 'obter arquivo.txt' :
    sentence = input('Erro, digite o comando novamente: ')

clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
modifiedSentence = clientSocket.recv(1024)

print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))

clientSocket.close() # encerramento o socket do cliente