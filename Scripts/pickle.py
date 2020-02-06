import pickle

arq = open('arquivo.pck','wb')
l1 = [1,2,3]

pickle.dump(l1,arq)
dump = pickle.dumps(l1)
print(dump)
arq.close()

arq = open('arquivo.pck','rb')

cont = pickle.load(arq)
print(cont)
arq.close()

class Pessoa(object):
    def __init__(self,nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def ola(self):
        print('Ola, eu me chamo %s'%self.nome)

arq = open('pessoa.pck','wb')
p = Pessoa('Gabriel Andrade')
pickle.dump(p,arq)
arq.close()

arq = open('pessoa.pck','rb')

p2 = pickle.load(arq)
print('\n',p2)
print(p2.nome)
print(p2.ola())
arq.close()

























