import sys
from Classes.conta import *

bradesco = Conta(1, 5000)
print(bradesco)
bradesco + 500
print(bradesco)
print(bradesco.__dict__) # retorna uo objeto no formato de dicionário
print(bradesco.__doc__) # retorna a documentação deixada na classe
print(bradesco.__init__.__doc__)

issubclass(classe_filha,classe_pai)
bradesco.__bases__
callable(bradesco)
dir(bradesco)
