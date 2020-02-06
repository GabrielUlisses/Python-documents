#del --> deletar
#is --> é

# -------------------- DEL IS -------------------- #
x = 10
print(x is 10)
print(x)

del x

try:
    print(x)
except:
    print('variável removido')
    
# -------------------- DEL DICTS -------------------- #

dic = {'a':10,'b':20,'c':30}
del dic['a']
print(dic)

# -------------------- DEL OBJECTS -------------------- #

class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def set_nome(self,nome):
        self.nome = nome
    
    def __str__(self):
        return 'Nome: %s Idade: %i'%(self.nome,self.idade)
        
p = Pessoa('Marccelo Carlos Pinha', 56)
print(p.idade)

del p.idade
try:    
    print(p.idade)
#del p.set_nome() #removendo método
except:
    print('atributo removido')
p.set_nome('Marcos Ribeiro Castro')
print(p.nome)


