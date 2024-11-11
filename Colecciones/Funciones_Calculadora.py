"""""
11/11/2024
Pograma de la funcionalidad de una calculadora
Se utilizan funciones para implementar el programa
"""""

#Funcion de una calculadora
def calculadora(opcion,num1,num2): #Declaración de la función la cúal tendra 3 parametros como argumento
# Logica de las distintas operaciones a implementar.
    if opcion==1:
        resultado=num1+num2
    elif opcion==2:
        resultado=num1-num2
    elif opcion==3:
        resultado=num1*num2
    elif opcion==4:
        resultado=num1/num2
    elif opcion==5:
        resultado=num1//num2
    elif opcion == 6:
        resultado = num1 % num2
    else:
        resultado= num1**num2
    return resultado

#Funcion que despliega el menu de operaciones
print("*** Calculadora utilizando funciones en Python ***")#Titulo que indica lo que hace el programa
print(" *** Programa del lic. Juan Bautista Juárez ***")
print()
def menu():#La función no recibe ningún parametro como argumento,solo imprime mensajes
    print("[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] División")
    print("[5] División entera")
    print("[6] Módulo")
    print("[7] Potenciación")
    print()

#Programa principal
menu() #Lamada a la función que despliega el menú
#solicitud de datos al usuario
opcion_operacion=int(input("Ingrese el numero de la operación: "))
num_1=float(input("Ingrese el primer número: "))
num_2=float(input("Ingrese el segundo número: "))
#Se llama a la función calculadora, proporcionandole los datos ingresadados por el usuario como argumento
print(f"El resultado es: {calculadora(opcion_operacion,num_1,num_2):.2f}")