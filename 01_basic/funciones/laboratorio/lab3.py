"""
Define un función llamada “promedio” que permita calculas el promedio de una lista.
La función debe recibir como argumento una lista de números enteros y 
retornar el promedio de dicha lista.
"""

def promedio(numeros=[]) -> float:
    return sum(numeros) / len(numeros)

print(promedio([1,2,3,4,5,6,7,8,9]))