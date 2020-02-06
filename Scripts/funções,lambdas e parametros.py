# O python aceita argumentos definidos antes dos indefinidos exe:.
# (n1, n2, *args)
# (*args, n1, n2) não é aceito

global valor 
valor = 10

def soma(*args):
    contador = 0
    for i in args:
        contador += i
    return contador

def divisao(num,div = 2):
    retorno = (num / div)
    return retorno

def controller(key,value,*args,**kwargs):
    value = value 
    def 1():
        nonlocal value
        print('protocolo 1')
    def 2():
        print('protocolo 2')
    def 3():
        print('protocolo 3')
    def 4():
        print('protocolo 4')
    def 5():
        print('protocolo 5')
    def 6():
        print('protocolo 6')
    key()
        
resultado = soma(1,2,3,4,5,6,valor)
a = divisao(resultado,4)
b = divisao(resultado)
f = (lambda y,x,z: x + y + z)
print(f(1,2,3))
print(resultado)
print(a,b)
