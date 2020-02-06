class contextManager:
    def imprime(self,msg):
        print("%s"%msg)
    def __enter__(self):
        print('Iniciando bloco')
        return self
    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)

with contextManager() as teste:
    teste.imprime('Olá')
    raise ValueError
