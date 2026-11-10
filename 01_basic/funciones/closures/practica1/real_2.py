"""
Ejercicio 2: Generador de IDs únicos incrementales

Contexto: 

Al crear registros en una base de datos o simular modelos,
necesitas un generador de identificadores únicos autoincrementales 
que no dependa devariables globales sueltas en el código.

Descripción: 

Diseña una función crear_generador_id(prefijo) que reciba una
cadena inicial (ej. "user", "prod"). Debe retornar una función sin 
argumentos que, cada vez que se invoque, devuelva un nuevo
ID concatenando el prefijo con un número secuencial único 
que empiece en 1 (ej. "user_1", "user_2").

Datos de entrada para probar:

generar_id_usuario = crear_generador_id("user")

generar_id_usuario() -> "user_1"
generar_id_usuario() -> "user_2"

generar_id_producto = crear_generador_id("prod")
generar_id_producto() -> "prod_1"
"""

from typing import Callable

def crear_generador_id(prefijo: str) -> Callable[[], str]:
    id = 1

    def generar_id() -> str:
        nonlocal id

        id_generado = f"{prefijo}_{id}"
        id += 1
        return id_generado

    return generar_id

generar_id_usuario = crear_generador_id("user")

print(generar_id_usuario())
print(generar_id_usuario())
print(generar_id_usuario())

generar_id_producto = crear_generador_id("prod")
print(generar_id_producto())
print(generar_id_producto())
