from socket import *

# Dados da conxao com o servidor

host = 'localhost'
port = 30800

socket_obj = socket(AF_INET, SOCK_STREAM) #protocolo ip, e servidor stream

socket_obj.bind((host,port))
socket_obj.listen(5)

# Testand a conexão com servidor

while True:  #enquanto houver conexão
    conexao, endereco = socket_obj.accept()
    print('O servior está conectado por',endereco)
    while True: # enqunato houver troca de dados
        data = conexao.recv(1024) # Libera 1024 bytes de conexão para o socket
        if not data:
            break
        conexao.send(b'Eco=>'+ data)
    conexao.close()
