"""
Ejercicio 2: El multiplicador acumulativo

Propósito: 

Practicar el uso de la palabra reservada nonlocal para modificar una
variable mutable o inmutable capturada del ámbito exterior.

Descripción: 

Diseña una función crear_multiplicador(factor) que tome un
número base. Debe retornar una función que reciba un número nuevo, 
lo multiplique por el factor guardado y acumule el resultado total 
de todas las llamadas sucesivas realizadas con esa función.

Datos de entrada para probar:

mult = crear_multiplicador(3)
Llamada 1: mult(2) -> Debería retornar
6 0 + (3 * 2)
Llamada 2: mult(4) -> Debería retornar
18 18 + (3 * 4)
Llamada 3: mult(1) -> Debería retornar
21 18 + (1 * 3)
"""

from typing import Callable

def crear_multiplicador(factor: int) -> Callable[[int], int]:
    acumulador = 0

    def multiplicar(numero: int) -> int:
        nonlocal acumulador

        acumulador += numero * factor

        return acumulador

    return multiplicar

mult = crear_multiplicador(3)

print(f"Total acumulado: {mult(2)}")
print(f"Total acumulado: {mult(4)}")
print(f"Total acumulado: {mult(1)}")
