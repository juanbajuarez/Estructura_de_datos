# Juan bautista Juarez
# 19 de noviembre  de 2024
# Tuplas ejemplo
"""
Ordenada
Inmutable
Los elementos se encierran entre parentesis
"""
print("**************************************************************")
print("Tupla primer ejemplo")
fechas_cumple=('12-19','12-27','01-10','10-18','11-01','09-30','08-25','01-06','10-21','04-11','03-06','08-02')
print(f"Las fechas de cumpleños son:{fechas_cumple}")

for fecha in fechas_cumple:
    print(fecha,end=" ")

print()
print("************************************************************")
print("Serie de pi de Leibniz")
pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,4/23)
print(f"suma con 3 elementos: {sum(pi_serie[0:2])}")
print(f"suma con 5 elementos: {sum(pi_serie[0:4])}")
print(f"suma con 8 elementos: {sum(pi_serie[0:7])}")
print(f"suma con 10 elementos: {sum(pi_serie[0:9])}")
print(f"suma con de todos los elementos: {sum(pi_serie)}")

print("*****************************************")
print("Ejemplo con cordenadas")
punto1=(1,0)
punto2=(5,3)
print(f"Cordenadas en tuplas: {punto1} y {punto2}")
x1,y1=punto1
x2,y2=punto2
print(f"La funcion de la recta es y={(y2-y1)/(x2-x1)}x{y1-((y2-y1)/(x2-x1))*x1}")

#punto1[0]=2
#punto1.append(2)