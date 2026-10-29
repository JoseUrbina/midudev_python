""" 
Ejercicio 2: Agrupamiento por propiedad

Escribe una función agrupar_por_edad(personas) que reciba una lista
de diccionarios donde c/elemento representa una persona con su nombre y edad.

La función debe retornar un diccionario donde:

- Las claves sean las edades presentes.
- Los valores sean listas con los nombres de las personas
    que tienen esa edad.
"""

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Sofia", "edad": 30},
    {"nombre": "Elena", "edad": 40}
]

def agrupar_por_edad(personas):
    agrupacion_edad = {}

    for persona in personas:
        edad = persona.get("edad")
        nombre = persona.get("nombre")
        
        agrupacion_edad[edad] = agrupacion_edad.get(edad, [])
        agrupacion_edad[edad].append(nombre)

    return agrupacion_edad

print(agrupar_por_edad(personas))
