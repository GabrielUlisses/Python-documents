#### TIME CLASS ####

import time

print(time.asctime()) # String contendo o tempo
#print(time.localtime()) # struct contendo dados sobre data e fuso 
#print(dir(time))
#print(help(time.strftime))
#time.process_time()
#time.gmtime()

a = time.localtime()
b = time.time()
c = time.struct_time()

print(f'Hora: {a[3]}hrs {a[4]}min')

time.sleep(2) # espera em segundos
