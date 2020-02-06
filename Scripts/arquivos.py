"""       """
# 'w' --> write
# 'r' --> read
# 'a' --> append
arquivo = open("teste.txt",'w') 
arquivo.write('E aí pessoal!\n')

arquivo.writelines(['e','ae?'])
arquivo.writelines(input("Digite algo para registrar:"))

arquivo = open('teste.txt','r')
print(arquivo.read())

arquivo.close()

# 'rb' --> read bytes
# 'wb' --> write bytes
arquivo = open('teste.txt', 'rb')
arquivo.seek(8) # percorre o numero de bytes informado
arquivo.tell() #  retorna o byte de leitura atual
arquivo.read(10) # apenas 10 bytes serão lidos 
arquivo.readlines(1) # apenas a primeira linha será lida
