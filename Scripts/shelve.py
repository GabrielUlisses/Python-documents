import shelve

class Pessoa:
    pass

marcela = Pessoa()
anael = Pessoa()
db = shelve.open('shelve.db')

# ==================== SALVANDO DADOS ==================== #

db['lista'] = [1,2,3,4,5]
db['pessoas'] = [marcela,anael]
db['anael'] = anael
db['marcela'] = marcela

print(db)

# ==================== ATUALIZANDO DADOS ==================== #

db['lista'].append(6) # não funciona
print(db['lista'])
x = db['lista']
x.append(6)

db['lista'] = x
print(db['lista'])

# ==================== REMOVER DADOS ==================== #

del db['anael']
print(db)

db.close()


# ==================== ATUALIZANDO DADOS - WRITEBACK ==================== #

db = shelve.open('shelve.db', writeback = True)

db['lista'].append(7)
print(db['lista'])

db.close()



















