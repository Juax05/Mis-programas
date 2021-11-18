import datetime
 
def edad(nacimiento):
    hoy = datetime.date.today()
    if hoy < nacimiento:
        print("hay un error en la fecha de nacimiento")
    else:
        año = nacimiento.year
        mes = nacimiento.month
        dia = nacimiento.day
 
        fecha = nacimiento
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(año+edad, mes, dia)
 
        print("tu edad es: %s" % (edad-1))

print("ingrese el año en el que usted nació")
año = int(input())
print("Ingrese el mes en el que nacio")
mes = int(input())
print("Ingrese el dia en el que nacio")
dia = int(input())

edad(datetime.date(año, mes, dia))
