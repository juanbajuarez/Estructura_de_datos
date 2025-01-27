from Examen_Parcial_3.gato_modulo import modos_juego

modos_juego()
def sprint(text:str, second:float)->None:
    """
    :param text:El título de juego a desplegar.
    :param second: El tiempo de retardo entre cada carácter.
    :return: No retorna ningún valor.
    """
    for line in text:
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(second)




def imprimir_titulo_ahorcado()->None:
    """
        Función para imprimir el título del juego del ahorcado.
        """
    dibujo = f"""
          {colored('AAAAA  H   H  OOOOO    RRRRR    CCCCC  AAAAA  DDDD   OOOOO    sssss', 'red')}
          {colored('A   A  H   H  O     O  R   R   C       A   A  D   D  O     O  s', 'cyan')}
          {colored('AAAAA  HHHHH  O     O  RRRRR   C       AAAAA  D   D  O     O  sssss', 'yellow')}
          {colored('A   A  H   H  O     O  R  R    C       A   A  D   D  O     O      s', 'blue')}
          {colored('A   A  H   H  OOOOO    R   R    CCCCC  A   A  DDDD   OOOOO    sssss', 'red')}
        """
    sprint(dibujo,0.01)