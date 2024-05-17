import matplotlib.pyplot as plt

x = [i for i in range(0, 10)]
print(x)

y = [xi**2 for xi in x]
print(y)

plt.plot(x, y)
plt.show()