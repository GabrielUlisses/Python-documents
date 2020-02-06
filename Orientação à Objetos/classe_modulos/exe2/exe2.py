class Obj2:
    
    def __init__(self,n,i=0): #se i não for informada, recebe 0 automaticamente
        self.nome = n
        self.idade = i
        print('Método construtor executado com sucesso!')

    def imprimeDados(self, *args): # *args: pode receber muitos argumentos de diversos tipos
        print('    Nome de Cliente: %s \n    Idade: %d'%(self.nome, self.idade))
        print(*args)
