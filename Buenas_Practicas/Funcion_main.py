from Funcion_modulo import menu
from Funcion_modulo import suma
from Funcion_modulo import resta


#Código a nivel de módulo.
if __name__ == '__main__':
    opcion=None
    while opcion!=0:
        opcion=menu()
        if opcion==1:
            print("Ingrese dos numeros a sumar")
            num1=float(input("Ingrese el primer número: "))
            num2=float(input("Ingrese el segundo número: "))
            print(suma(num1,num2))
        elif opcion==2:
            print("Ingrese dos numeros a restar")
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(resta(num1, num2))
        elif opcion ==0:
            print("Fin del programa.")
        else:
            print("Dato inválido.")

