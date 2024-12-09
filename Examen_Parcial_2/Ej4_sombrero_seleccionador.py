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
    val=None
    casas = [("Gryffindor",0) ,("Slytherin",0), ("Hufflepuff",0),("Ravenclaw",0)]
    while val> 4:
        for pregunta in preguntas:
            print(f"\n{pregunta[0]}")
            respuestas = pregunta[1:]
            for i, respuesta in enumerate(respuestas, 1):
                print(f"{i}) {respuesta[1]}")
            val = int(input("Selecciona tu respuesta"))
                if respuestas>4:
                    print()


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
        prueba(preguntas)
    elif opcion>1 or opcion<0:
        print("Opción no válida.")
    else:
        print("Programa Terminado")
        break
    print("***********************************************")