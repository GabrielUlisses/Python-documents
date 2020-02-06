class Conta:
    """
      Classe do tipo conta, seus atributos e métodos foram elaborados para simular umaconta bancária qualquer
    """
    def __init__(self, ID, saldo):
        """
        Metodo Construtor da classe Conta
        """
        self.ID = ID
        self.saldo = saldo
        
    def __str__(self):
        return 'ID: %s\nSaldo %.2f'%(self.ID, self.saldo)
    
    def __add__(self,valor): # automatiza operações de soma
        self.saldo += valor
    def __sub__(self,valor): # automatiza operações de subtração
        self.saldo -= valor
    def __div__(self,valor): # automatiza operações de divisão
        self.saldo /= valor
    def __mult__(self,valor): # automatiza operações de multiplicação
        self.saldo *= valor

    def __call__(self):
        return 'ID: %s'%(self.ID)
        
