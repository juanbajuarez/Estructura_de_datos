# Juan bautista Juarez
# 13 de noviembre  de 2024
#Listas ejercicio 3

def menu():
    print("[1] Ver calificaciones del alumno")
    print("[2] Ver promedio de alumnos")
    print("[3] Añadir alumno")
    print("[4] Eliminar alumno")
    print("[5] Ver promedio grupal")
    print("[0] Salir")

print(" *****Promedios parcial 1***** ")
opcion=1
alumnos=[]
estructura_datos = []
derecho=[]
contabilidad=[]
electronica=[]
algebra=[]
promedio=[]
cantidad_alumnos= 0

while opcion!=0:
    menu()
    opcion = int(input("Indique que accion desea realizar: "))
    if opcion==1:
        posicion=int(input("Indique la posicion de alumnos para mostrar sus datos: "))
        print("Nombre      ",alumnos[posicion-1])
        print("Estructura D",estructura_datos[posicion-1])
        print("Derecho     ",derecho[posicion-1])
        print("Contabilidad",contabilidad[posicion-1])
        print("Electronica ",electronica[posicion-1])
        print("Algebra     ",algebra[posicion-1])
    elif opcion==2:
        print(alumnos)
        print(promedio)

    elif opcion == 3:
        nombre=input("Ingrese el nombre del alumno:")
        alumnos.append(nombre)
        cal_estruc=float(input("Ingrese la calificacion de Estructura de datos: "))
        estructura_datos.append(cal_estruc)
        cal_der = float(input("Ingrese la calificacion de Derecho: "))
        derecho.append( cal_der)
        cal_cont = float(input("Ingrese la calificacion de Contabilidad: "))
        contabilidad.append(cal_cont)
        cal_elec = float(input("Ingrese la calificacion de Electronica: "))
        electronica.append(cal_elec)
        cal_alg = float(input("Ingrese la calificacion de Algebra: "))
        algebra.append(cal_alg)
        cantidad_alumnos+=1
        promedioA=(cal_estruc+cal_der+cal_cont+cal_elec+cal_alg)/5
        promedio.append(promedioA)

    elif opcion == 4:
        posicion = int(input("Indique la posicion de alumnos para eliminarlo: "))
        del alumnos[posicion-1]
        del estructura_datos[posicion-1]
        del derecho[posicion-1]
        del contabilidad[posicion-1]
        del electronica[posicion-1]
        del algebra[posicion-1]
    else:
        promedioG=sum(promedio)/cantidad_alumnos
        print(f"El promedio grupal es: {promedioG}")