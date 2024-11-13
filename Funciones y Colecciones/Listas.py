"""""
12/11/2024
Listas en Python
by Juan Bautista Juárez
"""""

#Crear lista

alumnos=[]
alumnos.append("Hector")
alumnos.append("Addi")
alumnos.append("Jesús Alberto")
alumnos.append("Juan")
print(alumnos)
print(alumnos[1])
alumnos.insert(1,"Tania")
for alumno in alumnos:
    print(alumno,end=" ")
alumnos.remove("Hector") #Para remover según su valor
print()
print(alumnos)
alumnos.pop(2) #Para remover por índice
print(alumnos)
del alumnos[2] #Para remover por índice
print(alumnos)

alumnos2=["Addy","Alberto","Bryan","Galilea","Hector","Jennifer","Juan","Louderes","Patricia","Rebeca","Rosalinda","Tania"]
len(alumnos2)
print(alumnos2)
alumnos2.sort()
print(alumnos2)
alumnos2.sort(reverse=True)
print(alumnos2)
print(alumnos2[-2])