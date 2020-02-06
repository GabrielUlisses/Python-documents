try:
    x = int(input('Digite um valor'))
except ValueError:
    print('Valor inválido')    
except:
    print('Erro não identificado')
    x = None
finally:
    print('procedimento encerrado')

try:
    raise ValueError
except (ValueError, IndexError, SyntaxError) as exception:
    print('Exceção capturada', exception)
    raise ValueError from exception

assert 10 > 0
x = 15
assert x>0 and x<20
assert x<10

x = open('arq.txt','w')
x.write("linha 01")
x.write("linha 02")
x.write("linha 03")
x.write("linha 04")
x.close()

with open('arq.txt') as arquivo:
    try:
        for linha in arquivo:
            print(linha)
    finally:
        arquivo.close()
