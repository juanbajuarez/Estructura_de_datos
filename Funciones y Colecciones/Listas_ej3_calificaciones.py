# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones con listas
# para implementar el control de calificaciones de un grupo.

#Función que muestra el menú.
def menu():
    print("*** Calificaciones del Parcial 1 ***")
    print("1) Ver calificaciones de todos los alumnos.")
    print("2) Ver calificaciones detalladas de un alumno.")
    print("3) Ver promedios del Parcial 1 de todos los alumnos.")
    print("4) Ver promedio grupal del Parcial 1.")
    print("5) Agregar alumno y sus calificaciones.")
    print("6) Eliminar alumno y sus calificaciones.")
    print("0) Salir.")
    opcion = int(input("Indique qué acción desea realizar: "))
    return opcion

#Función que muestra todos los alumnos.
def listar_alumnos(alumnos):
    tam = len(alumnos)
    for i in range(0, tam):
        print(f"{i + 1}) Nombre: {alumnos[i][0]}")
        print(f"   Derecho y legislación: {alumnos[i][1]}")
        print(f"   Estructura de datos: {alumnos[i][2]}")
        print(f"   Algebra lineal: {alumnos[i][3]}")
        print(f"   Electrónica: {alumnos[i][4]}")
        print(f"   Contabilidad: {alumnos[i][5]}")
        print()

#Función que muestra a un alumno.
def calificaciones_detalladas(alumnos):
    tam = len(alumnos)
    for i in range(0, tam):
        print(f"{i + 1}) {alumnos[i][0]}")
    pos = int(input("Seleccione el número del alumno para ver sus calificaiones: "))
    print(f"\nCalificaciones de {alumnos[pos-1][0]}:")
    print(f"Derecho y Legislación: {alumnos[pos-1][1]}")
    print(f"Estructura de Datos: {alumnos[pos-1][2]}")
    print(f"Álgebra Lineal: {alumnos[pos-1][3]}")
    print(f"Electrónica: {alumnos[pos-1][4]}")
    print(f"Contabilidad: {alumnos[pos-1][5]}")

#Función que muestra el promedio de cada los alumnos.
def promedios_individuales(alumnos):
    tam = len(alumnos)
    for i in range(0, tam):
        print(f"{i + 1}) {alumnos[i][0]}")
        print(f"   Promedio del parcial 1 es:{alumnos[i][6]:.1f} ")

#Función que muestra el promedio grupsl.
def promedio_grupal(alumnos):
    tam = len(alumnos)
    acumulador=0
    for i in range(0, tam):
        acumulador+=alumnos[i][6]
    promedio_grupal=acumulador/tam
    print(f"El promedio grupal del Parcial 1: {promedio_grupal:.1f}")

#Función para agrgar un nuevo alumno
def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    print("Ingrese las calificaciones del alumno:")
    derecho = float(input("  Derecho y Legislación: "))
    estructura = float(input("  Estructura de Datos: "))
    algebra = float(input("  Álgebra Lineal: "))
    electronica = float(input("  Electrónica: "))
    contabilidad = float(input("  Contabilidad: "))
    promedio=(derecho+estructura+algebra+electronica+contabilidad)/5
    alumnos.append((nombre, derecho, estructura, algebra, electronica, contabilidad,promedio))
    print(f"Alumno {nombre} añadido con éxito.")
    return 1

#Función para eliminar un alumno por su posición.
def eliminar_alumno(alumnos):
    tam = len(alumnos)
    for i in range(0, tam):
        print(f"{i + 1}) {alumnos[i][0]}")
    pos = int(input("Seleccione el número del alumno para ver sus calificaiones: "))
    alumnos.pop(pos-1)
    print("Alumno eliminado con éxito.")
    return 1

#Código a nivel de módulo.
print(" ***** Promedios Parcial 1 ***** ")
alumnos = []
opcion = None
alumnos_total=0
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        if alumnos_total==0:
            print("No hay alumnos")
        else:
            listar_alumnos(alumnos)
    elif opcion == 2:
        if alumnos_total==0:
            print("No hay alumnos")
        else:
            calificaciones_detalladas(alumnos)
    elif opcion == 3:
        if alumnos_total==0:
            print("No hay alumnos")
        else:
            promedios_individuales(alumnos)
    elif opcion == 4:
        if alumnos_total==0:
            print("No hay alumnos")
        else:
            promedio_grupal(alumnos)
    elif opcion == 5:
        alumnos_total+=agregar_alumno(alumnos)
    elif opcion == 6:
        if alumnos_total==0:
            print("No hay alumnos")
        else:
            alumnos_total-=eliminar_alumno(alumnos)
    elif opcion == 0:
        print("Programa Finalizado.")
    else:
        print("Opción no válida.")
    print("******************************")