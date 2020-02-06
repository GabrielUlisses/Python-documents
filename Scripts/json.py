#java script object notation serializaer = json

import json

contato = {
    'nome': 'marccelo palowisk cerrano',
    'telefone': '(45)9999-9999',
    'email': 'marcelo@email.com'
    }
json_obj = json.dumps(contato)
print(json_obj)

file = open('contato.json','wb')
file.write(json_obj.encode())
file.close()

lista = [1,2,3,4]
print(json.dumps(lista))

tupla = ('1','2','3','4')
print(json.dumps(tupla))

file = open('contato.json','rb')
data = file.readlines()

for item in data:
    print(json.loads(item))

class Pessoa(object):
    def __init__(self,nome,email,numero):
        self.nome = nome
        self.email = email
        self.numero = numero

    def __str__(self):
        return self.nome

p = Pessoa('GABRIEL','gabriel@email.com','(45)9999-9999')

print(json.dumps(p.__dict__))
