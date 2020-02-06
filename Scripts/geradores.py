# Um gerador consegue parar o seu programa e recuperar dados da execução(estado completo)

# objeto gerador --> possui protocolo de iteração, ou eja, é um objeto iterável, possuindo iterador.
# iterador --> __next__()

def gera_quadrados(n):
    for i in range(n):
        yeld i**2

for i in gera_quadrados(5)
    print(i)

x = gera_quadrados(5)

# expressões geradoras

"""
    enquanto as listas compressas são mais velozes e retornam os valores em lista,
    as expressões geradoras retornam um objeto gerador, que não armazena os valores
    na memória, apenas o objeto em questão

    listas compressas -> iteráveis mas não iteradores
    expressões geradoras -> iteráveis e iteradores | não pode ser convertida em lista
    
"""
l = (x**2 for x in range(10) if x%2 == 0)
print(l)
