# Juan bautista Juarez
# 12 de noviembre  de 2024
#Listas


def menu():
    print("[1] Ver lista de videos por añadidos")
    print("[2] Ver lista de videos por orden A-Z")
    print("[3] Ver lista de videos por orden A-Z")
    print("[4] Añadir video")
    print("[5] Añadir varios videos")
    print("[6] Eliminar video")
    print("[0] salir")

print("*** Vidios de tutub ***")
opcion=1
videos = []
videosT = 0
while opcion!=0:
    menu()
    opcion = int(input("Indique que accion desea realizar: "))
    if opcion==1:
        print(videos)
    elif opcion==2:
        videos.sort()
        print(videos)
    elif opcion==3:
        videos.sort(reverse=True)
        print(videos)
    elif opcion == 4:
        video=input("Ingrese el nombre del nuevo video: ")
        videosT+=1
        videos.append(video)
    elif opcion == 5:
        cantidad=int(input("Cuantos videos desea ingresar: "))
        while cantidad>0:
            nombre=input("Ingrese el nombre del video: ")
            videos.append(nombre)
            cantidad-=1
            videosT += 1
    elif opcion==6:
        del videos[videosT-1]
        videosT-=1
    print()
    print("**************************************")

