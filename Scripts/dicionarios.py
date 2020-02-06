"""       """
contato = {'Nome': 'Gabriel Ulisses', 'Celular' '9976-6160': '', 'Email' : 'ga@email.com'}

contato['Nome']
contato['Oficio'] = 'Estudante - Analista estagiário'

'Nome' in contato
'Endereco' in contato

contato_list = {}
contato_list[1] = contato

dic = {'f-acrescimo': lambda x: x+1, 'f-descrescimo': lambda x: x-1,'f-soma': lambda x,y: x+y,'f-subtracao' : lambda x,y: x-y}
dic['f-acrescimo'](5)
dic['f-soma'](5,10)


# ======================================== IMPRIMINDO CHAVES DE UM DICT ======================================== #
for chave in contato:
    print(chave)

# ======================================== IMPRIMINDO VALORES DE UM DICT ======================================== #

for chave in contato:
    print(contato[chave])

# ======================================== IMPRIMINDO CHAVES E VALORES DE UM DICT ======================================== #

for chave in contato:
    print(chave," ", contato[chave])

# ======================================== MÉTODOS ======================================== #

''' GET '''
contato.get('Nome')
contato.get('Nome', 'Valor não encontrado.')

''' ITEMS '''
contato.items() # retorna a chave e valor em formato de tupla dentro de uma lista

''' KEYS '''
contato.keys() # retorna uma lista contendo todas as chaves do dicionário

''' VALUES '''
contato.values() # retorna uma lista contendo todos os valores do dicionário

''' COPY '''
contato_backup = contato.copy() # copia os valores de contato para a variável em questão

''' POP '''
contato.pop('Celular')# retorna o valor indexado e remove ambos(key and value)

''' POPITEM '''
contato.popitem() #retorna a chave e o valor do primeiro elemento do dict em formato de tupla e em seguida os remove

''' CLEAR '''
contato.clear() # limpa os valores do dict

''' SETDEFAULT '''
contato.setdefault('Telefone','(45) 0000-0000') # define um valor padrão para chave, se esta não existir, ela será criada

''' DICT '''
dict() # cria um dicionario vazio
















]
