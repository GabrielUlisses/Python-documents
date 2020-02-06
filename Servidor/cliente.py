from socket import *

# Dados do cliente para conexao com o servidor

serverhost = 'localhost'
serverport = 30800
mensagem = [b'Ola, seja bem vindo!']

#cria o socket e conecta ao servidor
socket_obj = socket(AF_INET, SOCK_STREAM) #protocolo ip, e servidor stream

socket_obj.connect((serverhost,serverport))

for linha in mensagem:
    socket_obj.send(linha)
    #Resposta
    data = socket_obj.recv(1024)
    print('Cliente recebeu:',data)
    
socket_obj.close()
    
