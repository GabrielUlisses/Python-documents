nuns = [1,3,5,7]
lista = [1,2,3,4,[nuns]]
pares = [2,4,6,8,10]

print(lista)
print(lista[4][0:])

lista = lista + pares
lista.append(6)

print(lista)
print('valores totais da lista: %i \n o numero 6 se repete %i vezes'%(len(lista),lista.count(6)))
lista[::-1] # inverte os valores da lista
lista.remove(6)

print(lista)

lista.pop() # remove o último elemeno da lista
lista.pop(2) # remove o elemento no índice 2
lista.index(2)
a = lista.copy()

print(lista.index(2))

pares.sort()

print(lista)
print(lista.clear())

tupla = 1,2,3,4,5

a,b,c,d,e = tupla

