"""
Ejercicio 4: Uso de tuplas como Claves de Diccionario

En Python, las listas no pueden ser claves de un diccionario
porque son mutables. Las tuplas, al ser inmutables, sí se pueden 
usar como claves. Esto es ideal para representar grillas,
matrices o sistemas de reservas.

Objetivo:

Imagina un sistema de asientos de cine donde c/ asiento se identifica
por la tupla (fila, columna):

1. Crea un diccionario asientos donde las claves sean tuplas como
('A', 1), ('A', 2), ('B', 1) y los valores sean booleanos
(True si está ocupado, False si está libre).

2. Escribe una función reservar_asiento(asientos, asiento_tupla):
    - Si el asiento existe y está libre (False), cámbialo a True y retorna True
        (reserva exitosa).
    - Si ya está ocupado o no existe en la sala, retorna False
"""

asientos = {
    ("A", 1): True,
    ("A", 2): False,
    ("A", 3): True,
    ("B", 1): False,
    ("B", 2): False,
    ("B", 3): False
}

def reservar_asiento(asientos: dict, asiento_tupla: tuple) -> bool:

    if asiento_tupla in asientos:
        if asientos[asiento_tupla] == False:
            asientos[asiento_tupla] = True
            return True
        else:
            return False
    else:
        return False

print(asientos)

resultado = reservar_asiento(asientos, ("B", 1))

print("Reserva exitosa" if resultado else resultado)

resultado = reservar_asiento(asientos, ("A", 1))

print("Reserva exitosa" if resultado else resultado)

resultado = reservar_asiento(asientos, ("C", 1))

print("Reserva exitosa" if resultado else resultado)

print(asientos)
