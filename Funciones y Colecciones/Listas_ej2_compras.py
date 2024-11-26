# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones
# para implementar una lista de compras.

#Función que muestra el menú
def menu():
    print("[1] Ver lista")
    print("[2] Añadir producto a la lista")
    print("[3] Eliminar producto de la lista")
    print("[0] Salir")
    opcion = int(input("Indique qué acción desea realizar: "))
    return opcion

#Función que muestra todos los productos existentes en la lista.
def lista_productos(productos):
    tam = len(productos)
    for i in range(0,tam):
        print(f"{i + 1}) {productos[i][0]} ... {productos[i][1]}")

#Función que agrega productos de la lista.
def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    productos.append((nombre, cantidad))
    print(f"¡El producto [{nombre}, {cantidad}] ha sido añadido con éxito!")
    return 1

#Función que elimina productos de la lista.
def eliminar_producto(productos):
    lista_productos(productos)
    posicion = int(input("Indique el número del producto a eliminar: "))
    productos.pop(posicion-1)
    print("¡Producto eliminado correctamente!")
    return 1

#Código a nivel de módulo.
print("*** Lista de compras ***")
productos = []
opcion = None
total_p=0
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        if total_p==0:
           print("No hay productos para mostrar")
        else:
            lista_productos(productos)
    elif opcion == 2:
        total_p+=agregar_producto(productos)
    elif opcion == 3:
        if total_p==0:
           print("No hay productos para eliminar")
        else:
            total_p-=eliminar_producto(productos)
    elif opcion == 0:
        print("Fin del programa.")
    else:
        print("Opción no válida.")
    print("************************************")
