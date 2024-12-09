# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Exámen ejercicio número 4 "Test del sombrero seleccionador de Harry Potter"

#Función del menú.
def menu():
    print("***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***")
    print("1) Iniciar test.")
    print("0) Salir.")
    opcion=int(input("Ingresa una de las opciones: "))
    return opcion

#Función que realiza el test
def prueba (preguntas):
        c_mayor=[]
        casas_tupla = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}
        casas_diccionario=dict(casas_tupla)
        for pregunta in preguntas:
            print(f"\n{pregunta[0]}")
            respuestas = pregunta[1:]
            for i, respuesta in enumerate(respuestas, 1):
                print(f"{i}) {respuesta[1]}")
            validacion = True
            while validacion:
                val = int(input("Elige tu respuesta (1-4): "))
                if val > 4 or val < 1:
                    print("Númereo inválido.")
                    print(f"\n{pregunta[0]}")
                    respuestas = pregunta[1:]
                    for i, respuesta in enumerate(respuestas, 1):
                        print(f"{i}) {respuesta[1]}")
                else:
                    validacion=False
            #Incremeto a las casas según selección.
            num_casa = respuestas[val - 1][0]
            if num_casa == 0:
                casas_diccionario["Gryffindor"] += 1
            elif num_casa == 1:
                casas_diccionario["Slytherin"] += 1
            elif num_casa == 2:
                casas_diccionario["Hufflepuff"] += 1
            elif num_casa == 3:
                casas_diccionario["Ravenclaw"] += 1
        #La función max() en Python se utiliza para encontrar el valor máximo en
        # un diccionario, en una lista o en una tupla :
        # sintaxis max(iterable, key=function)
        c_mayor = max(casas_diccionario, key=casas_diccionario.get)
        cmayor=list(c_mayor)
        casas_lista = list(casas_diccionario.items())
        return  c_mayor

def preguntas_conjuntos(preguntas):

    preguntas_mezcladas = []
    for pregunta in preguntas:

        enunciado = pregunta[0]
        respuestas = pregunta[1:]
        respuestas_mezcladas = list(set(respuestas))
        pregunta_mezclada = [enunciado] + respuestas_mezcladas
        preguntas_mezcladas.append(pregunta_mezclada)
    return preguntas_mezcladas

# Código a nivel de módulo.
opcion = None
#Diccionario de preguntas.
preguntas = [
        ["¿Cuál de las siguientes opciones odiarías más que la gente te llamara?",
         (0, "Ordinario."), (1, "Ignorante."), (2, "Cobarde."), (3, "Egoísta.")],
        ["Después de tu muerte, ¿qué es lo que más le gustaría que hiciera la gente cuando escuche tu nombre?",
         (0, "Te extraña, pero sonríe."), (1, "Pide más historias sobre tus aventuras."),
         (2, "Piensa con admiración tus logros."),
         (3, "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.")],
        ["Dada la opción, preferirías inventar una poción que garantizara:",
         (0, "Gloria."), (1, "Sabiduría."), (2, "Amor."), (3, "Poder.")],
        ["¿Cómo te definirías en una sola palabra?",
         (0, "Valiente."), (1, "Ambicioso."), (2, "Leal."), (3, "Curioso.")],
        ["¿Qué cualidad te describe mejor?",
         (0, "La fuerza."), (1, "La astucia."), (2, "La paciencia."), (3, "La inteligencia.")]]
while opcion != 0:
    opcion = menu()
    if opcion==1:
        print("Tu casa es:",prueba(preguntas))
    elif opcion>1 or opcion<0:
        print("Opción no válida.")
    else:
        print("Programa Terminado")
        break
    print("***********************************************")