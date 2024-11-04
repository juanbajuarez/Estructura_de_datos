"""
Programa 2 del examen.
"""
print("**** Licenciatura en Informatica ***")
inicio=1
numero = int (input("Ingrese el numero final de la cuenta: "))

while inicio<=numero:
    if inicio%5==0 and inicio%3==0:
        print("Licenciatura en Informatica")
    elif inicio%5==0:
        print("Informatica",end=", ")
    elif inicio%3==0:
        print("Licenciatura",end=", ")
    else:
        print(f"{inicio}",end=", ")
    inicio+=1
