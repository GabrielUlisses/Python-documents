class MeuErro(Exception):
    def __init__(self,mensagem):
        self.mensagem = mensagem
    def __str__(self):
        return 'Erro: %s'%(self.mensagem)
    def erro(self):
        print("Erro comum")
    
try:
    raise MeuErro('valor inserido quebra a regra de negócio estabelecida')
except MeuErro as erro:
    print('encerrando',erro)
    
