import random
import msvcrt
import math

peliculas = ["Supercool", "Joker", "Avengers"]
precioEntrada = 350
descuento = False
Mayor = False
Miercoles = False
dia = random.randint(1, 7)

if dia == 3:
    Miercoles = True


print("Bienvenido al sistema digital de compra de entradas de cine")
print("Antes de comenzar indique su edad")
edad = int(input())
if edad >= 18:
    Mayor = True

print("para comenzar con la compra indiquenos que pelicula desea ver")
if Miercoles == True:
    print("Hoy es miercoles lo que significa que hay un 50% de descuento para menores de edad!!!")
if Miercoles & Mayor == True:
    print("Felicidades usted aplica para el 50% de descuento")
    descuento = True

print("Las peliculas disponibles el dia de hoy son estas:")
print(peliculas)
print("Si usted desea ver Supercool presione 1, si desea ver Joker presione 2 y si desea ver Avengers presione 3")
e = int(input())
if e == 1:
    print("usted eligió la pelicula Supercool")
    print("el precio es de 350 pesos")
    if descuento == True:
        precioEntrada = precioEntrada / 2
        print("Se aplico el descuento del 50%")

if e == 2:
    print("usted eligió la pelicula Joker")
    print("el precio es de 350 pesos")
    if descuento == True:
        precioEntrada = precioEntrada / 2
        print("Se aplico el descuento del 50%")

if e == 3:
    print("usted eligió la pelicula Avengers")
    print("el precio es de 350 pesos")
    if descuento == True:
        precioEntrada = precioEntrada / 2
        print("Se aplico el descuento del 50%")

print("con que metodo de pago desea pagar la entrada?")
print("Puede ser con tarjeta de credito o debito")
print("Presione 1 para continuar con el pago o 2 para cancelar el pago")
e = int(input())

if e == 1:
    print("Por favor ingrece los datos de la tarjeta a continuacion")
    print("Ingrese el numero de la tarjeta")
    numeroTarjeta = int(input)
    print("ahora ingrese el numero de seguridad que esta detras de la tarjeta")
    numeroAtrasTarjeta = int(input())
    print("ingrese la fecha de vencimiento MES/AÑO")
    fechaVencimiento = str(input())
    print("Ahora ingrese el nombre y el apellido del titular de la tarjeta")
    titularTarjeta = str(input())

    print("")
    print("Estos son los datos de la tarjeta")
    print("-----------------------------")
    print("numero de la tarjeta: ", numeroTarjeta)
    print("Numero de seguridad de la tarjeta: ", numeroAtrasTarjeta)
    print("Fecha de vencimiento de la tarjeta: ", fechaVencimiento)
    print("Titular de la tarjeta: ", titularTarjeta)
    print("-----------------------------")
    print("")
    print("Usted esta a punto de abonar: ", precioEntrada)
    print("")
    print("Presione 'Esc' para continuar...")
    key = None
    while key != '\x1b':
        key = msvcrt.getch()
    print("")
    print("su pago se esta procesando...")
    print("felicidades se ha completado la compra de las entradas")
    print("en breves se estaran imprimiendo")
    print("Muchas gracias por usar este programa y que disfrute de la pelicula")

if e == 2:
    print("Lamentamos que haya cancelado el pago")
    print("Esperamos que haya tenido una buena experiencia con este programa")
    print("Que tenga un buen dia/tarde/noche")






