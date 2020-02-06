from dataclasses import dataclass


"""Método clássico para definir classes de dados."""
class User:
    def __init__ (self,name:str,age:int,code:int):
        self.name = name
        self.age = age
        self.code = code

    def __repr__(self): # método para representar a classe
            return f'User(name={self.name},age={self.age},code={self.code})'

gabriel = User('Gabriel',25,111111)
print(gabriel)

@dataclass
class UserDt:
        name:str
        age:int
        code:int
        
gd = UserDt('gdDark',25,1111)

@dataclass
class Animal:
    def __init__(self,name,age,race):
        self.age = age
        self.name = name
        self.race = race
        
print(gd)
