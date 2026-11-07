"""
Ejercicio 6: Filtro dinámico por umbral

Propósito: 
Utilizar closures para configurar comportamientos de filtrado
de datos reutilizables.

Descripción: 
Escribe una función crear_filtro_mayor_que(limite) que retorne
una función capaz de recibir una lista de números 
y devolver una nueva lista únicamente con los elementos que sean
estrictamente mayores que el limite configurado.

Datos de entrada para probar:

filtro_mayores_a_10 =
crear_filtro_mayor_que(10)

datos = [4, 15,8, 23, 42, 10]
Llamada: filtro_mayores_a_10(datos)-> Resultado esperado: [15, 23, 42]
"""

from typing import Callable

def crear_filtro_mayor_que(limite: int) -> Callable[[list], list]:
    def filtrar_lista(numeros:list) -> list:
        return [numero for numero in numeros if numero > limite]

    return filtrar_lista

filtro_mayores_a_10 = crear_filtro_mayor_que(10)

datos = [4, 15,8, 23, 42, 10]

print(filtro_mayores_a_10(datos))
