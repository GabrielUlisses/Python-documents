# método __iter__ --> __next__

class Quadrados(object):
    """
        Este, suporta apenas uma iteração
    """
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self):
        if self.com < self.fim :
            self.com += 1
            return self.com**2
        else:
            raise StopIteration

x = Quadrados(0, 5)
l = list(x)
l1 = list(x)
print('listas do primeiro objeto',l,l1)

class Quadrados2(object):
    '''
        Este, suporta n iterações
    '''
    def __init__(self,com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        return Quadrados_iter(self.com, self.fim)

class Quadrados_iter(object):
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __next__(self):
        if self.com < self.fim:
            self.com += 1
            return self.com**2
        else:
            raise StopIteration

x = Quadrados2(0,6)
a = [print(i) for i in x]
b = [print(i) for i in x]

class Quadrados3(object):
    '''
        Este, permite n iterações devido à implementação de geradores
    '''
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        for i in range(self.com+1, self.fim+1):
            yeld i**2

x = Quadrados3(0,5)
a = [print(i) for i in x]
b = [print(i) for i in x]

print('listas 3',a,b)












        
 
