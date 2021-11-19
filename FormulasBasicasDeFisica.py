import math

def kineticEnergy():
    print("ingrese la masa en kg")
    mass = float(input())
    print("ingrese la velocidad en m/s**2")
    velocity = float(input())
    print("La energia kinetica en Joules(J) es:")
    print(0.5 * mass * velocity**2)

def newtons():
    print("ingrese la masa en kilogramos")
    mass = float(input())
    print("Ingrese la gravedad en m/s**2")
    print("La gravedad de la tierra es 9,807")
    gravity = float(input())
    print("El resultado de la masa en newtons es:")
    print(mass * gravity)

def energyAndWork():
    print("Ingrese el trabajo o la energia en Joules (J)")
    joules = float(input())
    print("Ingrese el tiempo en segundos")
    seconds = float(input())
    print("El poder en Watts(W) es:")
    print(joules / seconds)

def pressure():
    print("ingrese la fuerza en Newtons")
    newtons = float(input())
    print("ingrese el area en metros cuadrados")
    area = float(input())
    print("La presion en Pascals(P) es:")
    print(newtons / area)

print("Presione 1 para comenzar")
if int(input()) == 1:
    variable = True

while variable == True:
    print("Kinetic Energy formula: Presione 1")
    print("Kg a Newtons: Presione 2")
    print("Para calcular el poder en watts presione 3")
    print("Para calcular la presion oprima 4")
    print("si quiere salir del programa presione cualquier otro numero")
    r = int(input())
    if r == 1:
        kineticEnergy()
    if r == 2:
        newtons()
    if r == 3:
        energyAndWork()
    if r == 4:
        pressure()
    else:
        print("adios")
        break




