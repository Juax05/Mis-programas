print("Bienvenido al servicio de conversion de divisas de pesos argentinos. ¿Que divisa quiere convertir?")
print("Si quiere calcular dolar presione 1. Si quiere calcular euro presione 2")
respuesta = int(input("Presiona un numero del 1 al 2: "))

if respuesta == 1:
    cantidad = float(input("Cuanto dinero quiere calcular? en pesos argentinos: "))
    print(f"{cantidad} pesos son {round(cantidad / 167, 4)} dólares")

if respuesta == 2:
    cantidad = float(input("cuanto dinero quiere calcular? en pesos argentinos: "))
    print(f"{cantidad} pesos son {round(cantidad / 113.41, 4)} euros")