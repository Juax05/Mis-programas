import math

def areaCirculo(e):
    print(math.pi * e**2)

print("Digame el radio del circulo y yo le dire el area")
e = int(input())
areaCirculo(e)