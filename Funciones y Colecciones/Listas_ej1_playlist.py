# Autor: Juan Bautista Juárez
# Fecha: Noviembre de 2024
# Descripción: Programa en Python que utiliza funciones con listas
# para implementar una playlist de videos.


def menu():
    print("*** Playlist de videos de YouTube ***")
    print("1) Ver playlist por añadidos.")
    print("2) Ver playlist por orden ascendente A-Z.")
    print("3) Ver playlist por orden descendente Z-A.")
    print("4) Añadir video de YouTube a playlist.")
    print("5) Añadir varios videos de YouTube a playlist.")
    print("6) Eliminar video de la playlist.")
    print("0) salir.")

# Función para visualizar todos lo videos.
def listar_videos(videos):
    print("Lista de videos por añanidos:")
    tam=len(videos)
    for i in range(0,tam):
        print(f"{i+1}) {videos[i]}",end="\n")

# Función para visualizar todos lo videos de A-Z.
def verAZ_videos(videos):
    videos.sort()
    tam = len(videos)
    for i in range(0, tam):
        print(f"{i + 1}) {videos[i]}", end="\n")

# Función para visualizar todos lo videos de Z-A.
def verZA_videos(videos):
    videos.sort(reverse=True)
    tam = len(videos)
    for i in range(0, tam):
        print(f"{i + 1}) {videos[i]}", end="\n")

# Función para agregar un solo video.
def nuevo_video(videos):
    video = input("Ingrese el nombre del nuevo video: ")
    videos.append(video)
    print(f"!EL video {video} a sido añadido con éxito!")
    return 1

# Función para agregar  varios videos.
def nuevos_videos(videos):
    cantidad = int(input("Cuantos videos desea ingresar: "))
    videosT =0
    while cantidad>videosT:
        nombre = input(f"Ingrese el nombre del video {videosT+1} a agregar en la playlist: ")
        videos.append(nombre)
        videosT += 1
    print(f"¡Los {cantidad} videos han sido agregados con éxito!")
    return videosT

# Función para eliminar video por posición.
def eliminar_video(videos):
    listar_videos(videos)
    pos=int(input("Ingresa el índice del video a eliminar: "))
    del videos[pos-1]
    print("¡El video ha sido eliminado con éxito!")
    return 1


#Código a nivel de módulo.
opcion=None
videos = []
videosT = 0
while opcion!=0:
    menu()
    opcion = int(input("Indique que accion desea realizar: "))
    if opcion==1:
        if videosT==0:
            print("No hay videos para mostras.")
        else:
            listar_videos(videos)
    elif opcion==2:
        if videosT==0:
            print("No hay videos para mostras.")
        else:
            verAZ_videos(videos)
    elif opcion==3:
        if videosT==0:
            print("No hay videos para mostras.")
        else:
         verZA_videos(videos)
    elif opcion == 4:
        videosT+=nuevo_video(videos)
    elif opcion == 5:
        videosT+=nuevos_videos(videos)
    elif opcion==6:
        if videosT==0:
            print("No hay videos.")
        else:
            videosT-=eliminar_video(videos)
    elif opcion>6:
        print("Opcion inválida.")
    else:
        print("Fin del programa.")
    print("**************************************")