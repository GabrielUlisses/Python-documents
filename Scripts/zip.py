l1 = [1,2,3,4]
l2 = ['a','b','c','d','e']
zi = zip(l1,l2)
print(zi,'\n' + "%s"%list(zi)) # o zip encerra na primeira excessão 'StopInteration'

dic = dict(zip(l1,l2))
print(dic)
 
# ========== MAP ========== #
print('# ========== MAP ========== #\n')

l = [x**2 for x in range(4)]
l1 = map((lambda x: x**2),range(4))
l2 = map((lambda x,y: x+y),range(4),range(4))

def imprime(x,y):
    print(x,y)
    return x,y

l3 = map(imprime, range(4), range(3,-1,-1))

print(l,'\n%s'%map)
print(list(l1))
print(list(l2))
print(list(l3))

# ========== FILTER ========== #
print('\n# ========== FILTER ========== #\n')

f = filter((lambda x: x%2 == 0), range(5))
print(list(f))

# ========== MAP E FILTER ========== #
print('# ========== MAP E FILTER ========== #')
l4 = list(map((lambda x: x**2),filter((lambda x: x%2 == 0),range(10))))

print(l4)
