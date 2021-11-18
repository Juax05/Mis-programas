import os
import sys

lista = []

print("Ingrese una pelicula que le guste")
lista.append(str(input()))
print("estas son las peliculas que usted anoto")
print(lista)
print("Desea volver a utilizar el programa?")
r = int(input())
if r == 1:
    print(lista)
    python = sys.executable
    os.execl(python, python, *sys.argv)
else:
    print(lista)
    print("Gracias por utilizar el programa!")
    quit()