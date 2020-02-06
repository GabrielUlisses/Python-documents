class Pessoa(object):
    def __init__(self):
        self.__nome = "Marcelo Krabum"
        self.idade = 21
        self.sexo = 'M'
        self.altura = 170.20
        self.peso = 70.500
        
    def __str__(self):
        return self.nome
    
    def dados(self):
        print('Nome: %s\nIdade: %s \nSexo: %s \nAltura: %s \nPeso: %s'%(self.__nome,self.idade,self.sexo,self.altura,self.peso))
        
class funcionario(Pessoa):
    def __init__(self):
        self.cargo = "Analista"
        self.setor = "Desenvolvimento"
        
class Individuo:
    pass

i = Individuo()

p = Pessoa()
p.idade = 22
p.carro = "Monza"
p.dados()

print("\n====================  BREAK  ====================")

p.__nome = "gabriel"
p.dados()
print(p.__dict__)
