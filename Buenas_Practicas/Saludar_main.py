from Saludar_modulo import saludar


#Código a nivel de módulo.
if __name__ == '__main__':
    print(saludar.__name__)
    nombre = input("Ingrese un nombre:")
    saludar(nombre)