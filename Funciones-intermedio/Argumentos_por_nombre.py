def imprimir_alumno (nombre:str,edad:int,*,matricula:int,grupo:int,semestre:int=3)->None:
    print("Datos personales:")
    print(f"Nombre: {nombre}"
          f" Edad: {edad} "
          f" Matricula: {matricula}"
          f" grupo: {grupo}"
          f" Semestre: {semestre} ")

def main()->None:
    nombre="Juan Bautista Juárez"
    edad=25
    matricula=123456798
    grupo=303
    semestre=3
    #imprimir_alumno(nombre,edad,matricula,grupo)
    #imprimir_alumno(nombre="hola compa",matricula=123456789,edad=25,grupo=303,semestre=3)
    imprimir_alumno(nombre,edad,matricula=123456789,grupo=303,semestre=3)
# Código a nivel de módulo.
if __name__ == '__main__':
    main()