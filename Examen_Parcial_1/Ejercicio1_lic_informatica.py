"""
Programa 1 del examen.
"""
print("**** Licenciatura en Informática ****")
inicio = 1
numero = int(input("Ingrese el número final de la cuenta: "))

while inicio <= numero:
    if inicio % 5 == 0 and inicio % 3 == 0:
        print("Licenciatura en Informática")
    elif inicio % 5 == 0:
        print("Informática", end=", ")
    elif inicio % 3 == 0:
        print("Licenciatura", end=", ")
    else:
        print(f"{inicio}", end=", ")
    inicio += 1
