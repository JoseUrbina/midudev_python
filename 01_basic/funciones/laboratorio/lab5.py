"""
Define una función que nos permita conocer si todos los elementos de una lista son el mismo.
La función debe tener por nombre “iguales” y debe recibir como argumento un listado de
números enteros. La función debe retornar True o False si todos los elementos de la lista son el mimos.
- La función retornará None si la lista se encuentra vacía o solo posee un elemento.
"""

def iguales(numeros: list) -> None | bool:
    if len(numeros) < 2:
        return None

    i = 1

    while i < len(numeros):
        if numeros[i-1] != numeros[i]:
            return False

        i += 1

    return True
    
print(iguales([1,1,1,1,1,1,5,1,1,1]))
