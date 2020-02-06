
########## SYS ##########

import sys

# sys.platform --> retorna o sistema operacional
# sys.path --> todas as rotas relacionadas com a execução do programa
# sys.exit([args]) --> encerra a execução de um programa
# sys.modules --> todos os módulos carregados
# exc_info --> tupla que contém a ultima excessão levantada

if 'win' in sys.platform:
    import winsound

########## OS ##########

import os

#os.mkdir("Teste") --> Cria uma pasta
#os.getpid() --> id do processo em execução
#os.getcwd() --> diretório de trabalho
#os.rename("arquivo",'novo_nome') --> renomeia arquivo
#os.remove("arquivo") --> remove um arquivo
#os.path
#os.pathsep, os.sep, os.pards, os.curdir, os.linesep
#os.environ
#os.environ.keys()

########## OS.path ##########
#os.path.isdir("pasta") --> retorna uma expressão booleana 
#os.path.isfile("arquivo") --> retorna uma expressão booleana 
#os.path.exists("pasta") --> retorna uma expressão booleana 
#os.path.exists("arquivo") --> retorna uma expressão booleana 
#os.path.getsize("arquivo") --> retorna um inteiro representando o tamanho do arquivo em bytes
#os.path.split("C:\Users\Ulisses\Ulisses\Documentos\Python\Certificados") --> retorna um tupla separando caminho de diretório
#os.path.join("caminho","caminho") --> retorna um path composto pelos parâmetros informados
#os.path.dirname("caminho") --> retorna o diretório
#os.path.basename("caminho") --> retorna o arquivo ou diretório final do path
#os.path.splitext("arquivo ou caminho") --> retorna um tupla separando arquivo de extensão
#os.path.normpath("caminho") --> retorna o path com o separador "/ ou\" normalizado para a SO
#os.path.abspath("") --> retorna o caminho absoluto somado ao parâmetro
#os.path.abspath("ex") --> 
#os.path.abspath(".") --> retorna o arquivo ou diretório final do path
