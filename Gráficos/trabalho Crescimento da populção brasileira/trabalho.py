import matplotlib.pyplot as plt

dados = open('populacao-brasileira.csv').readlines()

x = []
y = []
labelx = "Ano"
labely = "População x1000.000.000"

title = "Crescimento da População Brasileira 1980-2016"


for i in range(len(dados)):
    if i != 0:
      linha = dados[i].split(";")
      x.append(int(linha[0]))
      y.append(int(linha[1]))

# plt.plot(x,y)
# plt.bar(x,y)
plt.scatter(x,y, s = 10)
plt.plot(x,y)
plt.title(title)
plt.xlabel(labelx)
plt.ylabel(labely)
plt.show()
