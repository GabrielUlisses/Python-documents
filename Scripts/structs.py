import struct
# Ns --> string de n char
# I --> inteiro pequeno
# Q --> inteiro grande
# f --> float pequeno
# d --> float grande
# ? --> valores Boolean

dic = {
    'nome': 'Max',
    'idade': 24,
    'peso': 79.40
    }
##            struct.pacotar('tipos dos valores', valores) 4s - str I - int f - float
cod = struct.pack('4s I f',dic['nome'].encode(), dic['idade'], dic['peso'])

print(cod)

arq = open('pessoas.cod','wb') #abre arquivo para escrita de bytes
arq.write(cod)
arq.close()

arq = open('pessoas.cod','rb')
cod_ab = arq.readline()
cod_desp = struct.unpack('4s I f',cod_ab)

print(cod_ab)
print(cod_desp,cod_desp[0],cod_desp[1],cod_desp[2])

nome = cod_desp[0].decode()
print(nome)

t = (b'Max', 25, 1.86)
s = struct.Struct('4s I f')
data = s.pack(t)

print(data)
s.unpack(data)
