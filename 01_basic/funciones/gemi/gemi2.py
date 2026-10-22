"""
Ejercicio 2: Filtrado de inventario por stock crítico

Estás trabajando en el sistema de un e-commerce. Tienes una lista de
diccionarios que representan los productos en stock y necesitas
filtrar cuáles necesitan reabastecimiento urgente (stock menor a 5 unds.)

Tarea:

Utiliza filter en combinación con una función lambda para obtener únicamente
los productos cuyo stock sea menor a 5.
"""

inventario = [
    {"nombre": "Teclado mecánico", "stock": 12},
    {"nombre": "Mouse inalámbrico", "stock": 3},
    {"nombre": "Monitor 24\"", "stock": 7},
    {"nombre": "Cable HDMI", "stock": 2},
    {"nombre": "Audífonos Gamer", "stock": 15}
]

reabastecer = lambda producto: producto.get("stock") < 5

productos_criticos = list(filter(reabastecer, inventario))

print(productos_criticos)
