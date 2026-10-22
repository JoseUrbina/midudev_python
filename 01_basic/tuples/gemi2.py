"""
Ejercicio 2: Procesador de métricas de servidor (retorno múltiple)

Un script de monitoreo lee métricas de CPU
a lo largo del tiempo guardadas en una lista.
Necesitas calcular estadísticas básicas y devolverlas
juntas en una sola tupla.

Objetivos:

1. Crea una función analizar_metricas(lecturas)
que reciba una lista de números.

2. Cálcula el valor mínimo, el valor máximo y el promedio.

3. Retorna los 3 valores en una sola tupla con el orden (min, max, promedio)

4. Muestra cómo llamar a la función desempaquetando el resultado
directamente en 3 variables (minimo, maximo, promedio)
"""

def analizar_metricas(lecturas:list) -> tuple:
    minimo = min(lecturas)
    maximo = max(lecturas)

    promedio = sum(lecturas) / len(lecturas)

    return minimo, maximo, promedio

minimo, maximo, promedio = analizar_metricas([42.2, 88.0, 12.5, 92.1, 60.3])

print(minimo, maximo, promedio)
