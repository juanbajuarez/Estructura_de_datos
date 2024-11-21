# Juan bautista Juarez
# 19 de noviembre  de 2024
# Tuplas con funciones


print(" Programa calificaciones del parcial ")

def calificacion(calificaciones):
    promedio_parcial=sum(calificaciones[0:3])/3
    promedio_final=(promedio_parcial+calificaciones[3])/2
    return promedio_parcial,promedio_final





print("Calificaciones de los parciales")
primer_parcial=float(input("Primer parcial: "))
segundo_parcial=float(input("Segundo parcial: "))
tercer_parcial=float(input("Tercer parcial: "))
ordinario=float(input("Ingrese su calificacion de ordinario: "))
calificaciones=(primer_parcial,segundo_parcial,tercer_parcial,ordinario)
tupla_2=calificacion(calificaciones)
print(f"El promedio parcial es: {tupla_2[0]:.1f} y el promedio final es: {tupla_2[1]:.1f}")
