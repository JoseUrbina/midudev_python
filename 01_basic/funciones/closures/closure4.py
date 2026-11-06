"""
Ejercicio 4: Generador de secuencias aritméticas

Propósito: 
Crear funciones con estado inicial y paso dinámico.

Descripción: 
Escribe una función crear_secuencia(inicio, paso) que
devuelva una función sin argumentos.
Cada vez que se invoque la función interna, debe retornar 
el siguiente valor de la secuencia aritmética (inicio, inicio +
paso, inicio + 2*paso, etc.).

Datos de entrada para probar:

s = crear_secuencia(10, 5)
Llamada 1: s() -> 10
Llamada 2: s() -> 15
Llamada 3: s() -> 20
"""

def crear_secuencia(inicio: int, paso: int):
    actual = inicio

    def siguiente():
        nonlocal actual

        valor_a_devolver = actual
        
        actual += paso
        return valor_a_devolver

    return siguiente

s = crear_secuencia(10, 5)
print(f"Valor actual: {s()}")
print(f"Valor actual: {s()}")
print(f"Valor actual: {s()}")
