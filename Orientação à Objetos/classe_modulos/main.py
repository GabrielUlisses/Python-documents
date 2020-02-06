import sys

sys.path.append('exe1')
print(sys.path)

from exe1 import *
from exe2.exe2 import *

print('Main está funcionando corretamente...')
Pedro = Obj1()
Pedro.imprimeDados()

pessoa = Obj2('Marcos Ribeiro da Figueira',25)
pessoa.imprimeDados()
