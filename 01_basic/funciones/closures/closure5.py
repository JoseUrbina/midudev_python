"""
Ejercicio 5: Historial de operaciones

Propósito: 
Almacenar colecciones (como listas) dentro del ámbito del closure para
mantener registro de la actividad.

Descripción: 
Diseña una función crear_acumulador_historial() que devuelva dos 
funciones empaquetadas o una función con un método/
comportamiento (puedes retornar una sola función que, según un argumento,
opere o devuelva el historial, o bien usar una función que guarde operaciones).

Tip: 
Para mantenerlo simple como closure puro, haz que la función devuelva
una función que al llamarla con un número lo sume al total y guarde la
operación en una lista interna, y si sellama sin argumentos (o con un comando
especial), devuelva el historial completo.

Alternativa limpia y sencilla para este nivel: 

Crea una función crear_caja_fuerte() que retorne una función para 
depositar(monto) y otra para consultar_historial(). (Nota: En Python
puedes retornar una tupla de funciones o un diccionario que comparten el mismo
ámbito léxico).

Datos de entrada para probar:

depositar, ver_historial =
crear_caja_fuerte()

Llamada 1: depositar(100) -> Registra
depósito de 100

Llamada 2: depositar(50) -> Registra
depósito de 50

Llamada 3: ver_historial() -> Debe
retornar una lista con las operaciones osaldos, ej: [100, 50]
"""

from typing import Callable

def crear_caja_fuerte() -> tuple[Callable[[float], str], Callable[[], list]]:

    saldos = []

    def depositar(monto: float) -> str:
        saldos.append(monto)
        return f"Se registro un depósito de {monto}."

    def consultar_historial() -> list:
        return saldos

    return depositar, consultar_historial

depositar, ver_historial = crear_caja_fuerte()

print(depositar(100))
print(depositar(50))

print(f"Historial de saldos: {ver_historial()}")
