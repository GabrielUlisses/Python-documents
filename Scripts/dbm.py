
# c --> create cria o database, se está já existir apenas a abrirá
# r --> read
# w --> write
# n --> new cria um novo database para leitura e escrita 

import struct
import dbm

db = dbm.open('contatos.db','c')

contato = {}
contato['nome'] = 'GABRIEL ANDRADE'
contato['email'] = 'gabriel@email.com'
contato['celular'] = '(45)9999-9999'
contato['idade'] = '25' # valores precisam ser strings ou bytes

db['nome'] = contato['nome']
db['email'] = contato['email']
db['celular'] = contato['celular']
db['idade'] = contato['idade']

print(db['nome'])
print(db['nome'].decode())
print(db)
print('%i'%int(db['idade']))

print(db.keys())
print(b'GABRIEL ANDRADE' in db['nome'])

del db['email']

db.pop('idade')

db['n_registro'] = struct.pack('I',55674)

print(db.keys(),' n_registro:',db['n_registro'])

db.close()
