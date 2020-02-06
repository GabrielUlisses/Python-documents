class Pessoa(object):
    def __init__(self,nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        
    def __str__(self):
        return self.nome
    
    def dados(self):
        print('Nome: %s\nIdade: %s \nSexo: %s \nAltura: %f'%(self.nome,self.idade,self.sexo,self.altura))
        
class Funcionario(Pessoa):
    def __init__(self,pessoa,cargo,setor):
        #super(Pesssoa, self).__init__(nome,idade,sexo,altura)
        self.pessoa = pessoa
        self.cargo = cargo
        self.setor = setor

    def dados(self):
        #super(Pessoa,self).dados()
        #super().dados()
        self.pessoa.dados()
        print('Cargo: %s \nSetor: %s \n'%(self.cargo, self.setor))

marcelo = Pessoa("Marcelo Freitas Filho",22,'M',172)
marcelo.dados()
print('\n BREAK \n')
marcelo = Funcionario(marcelo,"Analista","Desenvlvimento")
marcelo.dados()
