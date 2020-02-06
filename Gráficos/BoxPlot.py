import matplotlib.pyplot as plt
import random

titulo = "Boxplot" 
vetor = []

for i in range(100):
    numeros = random.randint(0,200)
    vetor.append(numeros)
    
plt.title("BoxPlot")
plt.boxplot(numeros)
plt.show()
