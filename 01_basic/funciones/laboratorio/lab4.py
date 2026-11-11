"""
Define una función que permita conocer si el primer y
último elemento de una lista son el mismo elemento.
La función debe tener por nombre “iguales”.
La función debe recibir como argumento una lista de números
enteros con longitud mayor a 2. La función debe retornar
verdadero o falso si el primer y último elemento son el mismo número.

- Si la función recibe una lista con 2 o menos elementos retornará None.
"""

def iguales(numeros: list) -> None | bool:
    if len(numeros) <= 2:
        return None

    return numeros[0] == numeros[-1]

print(iguales([1,3,4,5,6,7,0]))
