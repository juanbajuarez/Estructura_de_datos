
#Función saludar.
def saludar(nombre:str)-> None:
    print(f"Hola {nombre}")

    """
       Función que imprime un nombre.
       :param cadena:  Nombre que se implementara.
       :return: nada.
       """

#Código a nivel de módulo.
if __name__ == '__main__':
    nombre=input("Ingrese un nombre:")
    saludar(nombre)