lista = ["Sumo", "Divididos", "Seru Giran", "Los Piojos", "ACDC"]
print("Procedere a imprimir sus artistas favoritos")
print(lista)

r = int(input(("Desea agregar mas artistas a la lista? presione 1 para si y cualquier otra cosa para no")))

if r == 1:
    print("Digame los artistas que desea agragar")
    ext = input()
    lista.extend([ext])
    print("esta es su nueva lista")
    print(lista)