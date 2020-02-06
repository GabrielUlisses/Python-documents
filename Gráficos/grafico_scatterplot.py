import matplotlib.pyplot as plt
x = [2,3,4]
y = [20,25,24]
z = [10,30,50]
titulo = "Grafico Scatterplot"
eixoX = "Tempo (mês)"
eixoY = "% de investimentos"

plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)


for i in range(0, len(y)-1):
    if y[i] > 20:
       color = 'r'
       print(y[i])
    else :
       color = 'g'
       
plt.scatter(x,y, label = "pontuação", color=color, s = z) # cria gráfico de pontos
plt.plot(x,y) # liga os pontos
plt.savefig("nome_da_figura.png", dpi =400) # salva como .pdf ou .png 'dpi' representa o tamanho da imagem
plt.show()

