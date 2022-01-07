import matplotlib.pyplot as plt

print("ingrese un valor")
n = int(input())
lista = list()
print("ingrese un valor p")
x = [1, 2, 3, 4, 5, 6, 7]
y = list()

while n > 1:
    if n % 2 == 0:
         n = n / 2
         lista.append(n)
         y.append(n)
    else:
         n = 3 * n + 1
         lista.append(n)
         y.append(n)
print(lista)

count = 0
for element in y:
     count += 1

x = range(count)

plt.plot(x, y)
plt.xlabel('Orden')
plt.ylabel('Valor')
plt.title('3n+1')
plt.show()