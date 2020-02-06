string = """
interessante,
como o python trabalha com strings
de uma maneira versátil        ."""

print(string, end = '   ')
print('Basquete')

lista = ['P','e','d','r','o']

for char in lista:
    print(char,end = '')
    
print('\n')
    
for char in 'Pedro':
    print(char)
    
"""
Strings e Bytes
"""

string = 'basquete'
byte = b'basquete'
print('%s %s'%(string, type(string)),'%s %s'%(byte, type(byte)))

string = 'se liga'
x = string.encode()

print(string.encode()) # string sendo convertida para string bytes
print(x.decode()) # string sendo convertida para string bytes

"""
Tabela ASCII
"""
ascii_array = []
for i in range(256):
    print("%.3i - %s"%(i,chr(i)))
    ascii_array.append(chr(i))
    #print("%.3i - %c"%(i,i))

for i in ascii_array:
    print("%s - %s"%(ord(i),i))
