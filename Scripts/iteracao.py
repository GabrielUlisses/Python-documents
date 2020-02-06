# objetos iteraveis - que podem ser percorridos por um loop for(iterador)

import random

#métodos:
#__next__

arq = open('teste.txt', 'w')
arq.write(' linha 1: Ola Mundo!\n')
arq.write(' linha 2: Estou Feliz em saudá-los!\n')
arq.write(' linha 3: Tudo bem com vocês?\n')
arq.write(' linha 4: ...\n')
arq.write(' linha 5: Tchau ;-;\n')
arq.close()


x = open('teste.txt')
print(x.__next__(),'\n',x.__iter__())
x.close()

x = open('teste.txt')
print(next(x))
print(iter(x))
x.close()
#==================== COMPRESSÃO DE LISTA ====================#

lista = [x + 10 for x in range(10)]
l = [x + y for x in 'abc' for y in 'lmn']

# x + 10 --> expressão
# for x in range --> iterador
# range(10) --> Objeto iterável

print(lista,'\n',l)

#==================== COMPRESSÃO DE LISTA - ARQUIVOS ====================#

#arq = open('teste.txt')
#l = arq.readlines()
#l = [print(linha.rstrip()) for linha in l]

l = [print(linha.rstrip()) for linha in open('teste.txt')]

#==================== COMPRESSÃO DE LISTA - CLAUSULA IF ====================#


l = [random.randint(1,100) for i in range(30) if i%2==0]
print(l)

l = [x for x in l if x%2==0]
print(l)



















