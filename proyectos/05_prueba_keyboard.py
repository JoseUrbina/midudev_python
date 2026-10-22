# Cronómetro deportivo

import time
# pynput: permite controlas y monitorear los dispositivos de entrada de tu computadora (teclado/mouse)
from pynput.keyboard import Key, Listener

tecla_detectada = None

def al_presionar(tecla):
    global tecla_detectada
    try:
        tecla_detectada = tecla.char.lower() # Guarda letras o números
    except AttributeError:
        tecla_detectada = tecla      # Guarda teclas especiales (Ctrl, Enter, etc.)

    # Retornar False detiene el listener inmediatamente tras la primera pulsación
    return False

print("Presiona la barra espaciadora para activar el turbo. Presiona 'q' para salir.")

while True:
    # suppress: evita que las teclas se escriban en la pantalla
    # on_press: se activa al pular una tecla
    # Listener: escucha los eventos globales del teclado del o.s
    with Listener(on_press=al_presionar, suppress=True) as listener:
        listener.join()

    if tecla_detectada == Key.space:
        print("¡Turbo activated!")

    if tecla_detectada == "q":
        print("Good Bye :)")
        time.sleep(0.5)
        break
