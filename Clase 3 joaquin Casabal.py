print("Decime un numero y yo te digo si es par o no")
numero = float(input())
resultado = divmod(numero, 2)
if resultado == 0:
    print("El numero es par")
else:
    print("El numero es impar")