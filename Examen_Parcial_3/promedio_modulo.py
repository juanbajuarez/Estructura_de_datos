from Funciones_examen_modulo import nombre,valida_nombre,valida_numeros
def menu_promedio()->int:
    """

    :return:
    """
    print("Menu para calcular el promedio de un alumno")
    print("1) Calcular el promedio de un alumno")
    print("0) Salir")
    opcion = input("Ingrese el número de la acción deseada: ")
    while not (opcion.isnumeric() and 0 <= int(opcion) <= 1):
        print("Opción no válida")
        print("*************************************")
        print("1) Calcular el promedio de un alumno")
        print("0) Salir")
        opcion = input("Ingrese el número de la acción deseada: ")
    opcion = int(opcion)
    return opcion

def cal_promedio(Nombre:str,**kwargs)->None:
    """

    :param Nombre:
    :param kwargs:
    :return:
    """
    print("Nombre:",Nombre)
    suma_calificaciones=0
    promedio=0
    for materia, calificacion in kwargs.items():
        print(f"Materia: {materia}, Calificación: {calificacion}")
        suma_calificaciones+= calificacion
    promedio=suma_calificaciones/5
    print(f"El promedio obtenido es: {promedio:.2f}")

def datos_promedio ()->None:
    """

    :return:
    """
    nom = nombre()
    algebra = input("Ingrese la calificación de Algebra Lineal: ")
    algebra = valida_numeros(algebra)
    while algebra is None or not (0 <= algebra <= 10):
        print("Dato invalido")
        algebra = input("Ingrese una calificación valida: ")
        algebra = valida_numeros(algebra)

    electronica = input("Ingrese la calificación de Electrónica: ")
    electronica = valida_numeros(electronica)
    while electronica is None or not (0 <= electronica <= 10):
        print("Dato invalido")
        electronica = input("Ingrese una calificación valida: ")
        electronica = valida_numeros(electronica)

    contabilidad = input("Ingrese la calificación de Contabilidad: ")
    contabilidad = valida_numeros(contabilidad)
    while contabilidad is None or not (0 <= contabilidad <= 10):
        print("Dato invalido")
        contabilidad = input("Ingrese una calificación valida: ")
        contabilidad = valida_numeros(contabilidad)

    derecho = input("Ingrese la calificación de Derecho: ")
    derecho = valida_numeros(derecho)
    while derecho is None or not (0 <= derecho <= 10):
        print("Dato invalido")
        derecho = input("Ingrese una calificación valida: ")
        derecho = valida_numeros(derecho)

    estructuras = input("Ingrese la calificación de Estructura de datos: ")
    estructuras = valida_numeros(estructuras)
    while estructuras is None or not (0 <= estructuras <= 10):
        print("Dato invalido")
        estructuras = input("Ingrese una calificación valida: ")
        estructuras = valida_numeros(estructuras)
    cal_promedio(nom, algebra=algebra, electronica=electronica, contabilidad=contabilidad, derecho=derecho,
                 estructuras=estructuras)