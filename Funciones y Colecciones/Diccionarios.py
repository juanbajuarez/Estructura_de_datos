# Autor: Juan Bautista Juárez
# Fecha: Diciembre de 2024
# Descripción: Introduccion a diccionarios en Python.

"""
Por clave-valor
Ejemplos de usos
nombre_diciionarios={'key':"valor",'key2':"valor2"}
"""
#Declaracion de los diccionarios
diccionario_profesor={'nombre': "Juan",'primer_apellido':"Bautista",'edad':"24",'correo': "juanb8935@gmail.com",'cubo':100}
diccionario_juan={}

#añadiendo valor al diccionario
diccionario_juan['nombre']="Juan"
diccionario_juan['primer_apellido']="Bautista"
diccionario_juan['segundo_apellido']="Juarez"
diccionario_juan['grupo']="303"

#Impresion de los valores del diccionario
print(diccionario_profesor)
print(diccionario_juan)

#Acceso a los valores del diccionario mediante las claves
nombre_alumno=diccionario_juan.get('nombre')
print(nombre_alumno)
apellido_alumno=diccionario_juan['primer_apellido']
print(apellido_alumno)

#Diccionario antes de modificarlo
print(diccionario_juan)

#Cambio de valores  a los campos del diccionario
diccionario_juan['nombre']="El ing"
diccionario_juan['grupo']=403

#Diccionario despues de modificarlo
print(diccionario_juan)

#Añadiendo nuevos valores al diccionario
diccionario_juan['materia_favorita']="Algebra lineal"
print(diccionario_juan)

#Eliminar valores mediante key manera 1
del diccionario_juan['segundo_apellido']

#Eliminar valores mediante key manera 2
diccionario_juan.pop('grupo')

print(diccionario_juan)

#Acceso al diccionario mediante ciclo for a las claves y su valor
for clave,valor in diccionario_juan.items():
    print(f"Clave: {clave} y valor: {valor}")

#Acceso al diccionario mediante ciclo for a los valores
for valor in diccionario_juan.values():
    print(f"valor: {valor}")

# Acceso al diccionario mediante ciclo for a las claves
for clave in diccionario_juan.keys():
    print(f"clave: {clave}")

#Combinación con tuplas
diccionario_egresados={'nombre':"Eliezer", ('primer_a','segundo_apellido'):"P_ys",'edad':23}
print(diccionario_egresados)

#Acceso al diccionario mediante ciclo for a las claves y su valor diccionario egresado
for clave,valor in diccionario_egresados.items():
    print(f"Clave: {clave} y valor: {valor}")

#Diccionario de la carrera de informanita
diccionario_informatica={'grupo_303':{'no_alumnos':12,'no_materias':5,'promedio_grupal':7.99},'grupo_503':{'no_alumnos':7,'no_materias':5,'promedio_grupal':6},'grupo_703':{'no_alumnos':7,'no_materias':5,'promedio_grupal':8},'grupo_903':{'no_alumnos':2,'no_materias':5,'promedio_grupal':5}}
print(diccionario_informatica)

#Acceso al diccionario mediante ciclo for al diccionario inforamtica
for grupo in enumerate(diccionario_informatica):
    print(f"grupo: {grupo}")

#acceso los promedios por semestre
prom_303=diccionario_informatica['grupo_303']['promedio_grupal']
prom_503=diccionario_informatica['grupo_503']['promedio_grupal']
prom_703=diccionario_informatica['grupo_703']['promedio_grupal']
prom_903=diccionario_informatica['grupo_903']['promedio_grupal']
print(prom_303)
print(prom_503)
print(prom_703)
print(prom_903)