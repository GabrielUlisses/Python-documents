import random


#random.randrange(start,stop[,step])

#random.randrange(a, b) função a <= N < b
for i in range(10):
    x = random.randrange(1,8)
    y = random.randrange(1,7,2)
    print("%s, %s"%(x,y))
    
print("\n")

#random.randrange(a, b) função a <= N <= b
for i in range(10):
    x = random.randint(1,8)
    print("%s"%(x))
    
print("\n")

#random.choice(seq) valor aleatória da sequência
for i in range(10):
    x = random.choice([0,1,2,3,4,5,6,7,8,9,10])
    print("%s"%(x))

print("\n")
 
#random.random() valor real entre 0.0 e 1.0
for i in range(10):
    x = random.random()
    print("%s"%(x))
    
print("\n")
 
#random.uniform(a,b) a <= N <= b ou b <= N <= a
for i in range(10):
    x = random.uniform(1,7)
    print("%s"%(x))