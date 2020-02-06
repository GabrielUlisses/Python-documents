import matplotlib.pyplot as plt

x1 = [1,3,5]
x2 = [2,4,6]

y1 = [20,30,24]
y2 = [40,34,22]

plt.xlabel("mês")
plt.ylabel(' % lucro')

plt.bar(x1,y1, label = "empresa 01")
plt.bar(x2,y2, label = "empresa 02")
plt.show()

