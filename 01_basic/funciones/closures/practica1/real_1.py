"""
Ejercicio 1: Caché de rendimiento o Memoización

Contexto: 

En una aplicación web, a veces tienes funciones que realizan cálculos
matemáticos pesados o consultas repetitivas. Para no recalcular lo 
mismo una y otra vez, guardas en memoria los resultados anteriores.

Descripción: 

Escribe una función fábrica crear_calculadora_con_cache() que
contenga un diccionario interno vacío. La función debe retornar 
una función interna que reciba un número x, verifique si el
resultado de elevar al cuadrado (x ** 2) ya está guardado en el diccionario:
Si ya existe, debe retornar el valor almacenado imprimiendo un mensaje de
que vino del caché (ej. "[Caché hit]").
Si no existe, lo calcula, lo guarda en el diccionario para futuras ocasiones y lo
retorna (ej. "[Calculando nuevo]").

Datos de entrada para probar:

calcular = crear_calculadora_con_cache()

calcular(4) -> Debería calcular y retornar 16

calcular(4) -> Debería retornar 16
(leyéndolo directamente del caché)

calcular(5) -> Debería calcular y retornar 25
"""

def crear_calculadora_con_cache():
    cache_de_numeros = {}

    def calcular_cuadrado(numero: int):

        # Búsqueda de la existencia del número en el diccionario
        if numero in cache_de_numeros.keys():
            return f"[Caché hit] {cache_de_numeros.get(numero)}"

        # Calculando y guardando una nueva llave en el diccionario con su respectivo valor
        cache_de_numeros[numero] = numero ** 2

        return f"[Calculando nuevo] {cache_de_numeros.get(numero)}"

    return calcular_cuadrado

calcular = crear_calculadora_con_cache()

print(calcular(4))

print(calcular(4))

print(calcular(5))
