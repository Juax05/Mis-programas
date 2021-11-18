def BTC(ahorro):
    return ahorro / 6212956.42

def ETH(ahorro):
    return ahorro / 436257.64

def LTC(ahorro):
    return ahorro / 25031.47

print("Ingrese la cantidad de dinero que tiene para invertir")
print("Ingrese la cantidad de dinero en pesos")
ahorro = int(input())
print("Usted dispone de un ahorro en pesos de:")
print(ahorro)
print("Usted con su dinero a dia de hoy puede comprar esta cantidad de bitcoin:")
print(BTC(ahorro))
print("Y esta es la cantidad de ethereum que puede comprar con su dinero:")
print(ETH(ahorro))
print("y no olvide que puede comprar esta cantidad de litecoin con su dinero")
print(LTC(ahorro))