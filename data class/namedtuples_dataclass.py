from typing import NamedTuple
from collections import namedtuple

user = namedtuple('User','name age code') #namedtuple pode ser acessado porindices
gabriel = user('Gabriel',18,123333)

class User(NamedTuple): 
    """Classe que extende de namedtuple"""
    name : str
    age : int
    code : int

User = NamedTuple('User2',[('name',str),('age',int),('code',int)])
c = User('example',22,233445)

jh = ('jhon',680,1111)

print(c)
print(gabriel)
print(jh[0],jh[1],jh[2])
