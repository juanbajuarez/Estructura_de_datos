


def juego_del_gato()->None:
    from gato_modulo import usuario_vs_usuario, usuario_vs_cpu
    from gato_modulo import modos_juego
    modo=modos_juego()
    if modo==1:
        usuario_vs_usuario()
    elif modo==2:
        usuario_vs_cpu()
    else:
        print("Saliendo del juego")