# Juan bautista Juarez
# 13 de noviembre  de 2024
#Listas ejercicio 2


def menu():
    print("[1] Ver lista")
    print("[2] Añadir producto a la lista")
    print("[3] Eliminar de la a la lista")
    print("[0] Salir")

print("***Lista de compras***")
opcion=1
nombre_productos = []
cantidad_productos=[]
cantidad_t= 0
while opcion!=0:
        menu()
        opcion = int(input("Indique que accion desea realizar: "))
        if opcion==1:
            print(nombre_productos)
            print(cantidad_productos)
        elif opcion==2:
            nombre_producto=input("Ingrese el nombre del producto: ")
            cantidad_producto=input("Ingrese la cantidad: ")
            nombre_productos.append(nombre_producto)
            cantidad_productos.append(cantidad_producto)
            cantidad_t+=1
        else:
            del nombre_productos[cantidad_t-1]
            del cantidad_productos[cantidad_t-1]
        print("************************************")