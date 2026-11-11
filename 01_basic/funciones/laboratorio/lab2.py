"""
Define una función que permita conocer cuantas vocales posee un string.
La función debe tener por nombre “vocales” y debe recibir como argumento
un string. La función debe retornar la cantidad de vocales que dicho string posee.
"""

def vocales(cadena: str) -> int:
    cantidad_vocales = 0

    for c in cadena:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            cantidad_vocales += 1

    return cantidad_vocales

print(vocales("hola mundo nuevamente"))
