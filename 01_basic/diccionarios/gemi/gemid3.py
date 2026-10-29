"""
Ejercicio 3: Inversión y fusión de diccionarios

Imagina que tienes 2 diccionarios que representan el inventario de 2 sucursales
de una tienda:

Escribe una función fusionar_y_filtrar(inventario_a, inventario_b, umbral_minimo) que:

1. Combine ambos inventarios sumando las cantidades de los productos que aparezcan
    en ambas sucursales.

2. Elimine del inventario final cualquier producto cuya suma total sea estrictamente
    menor que umbral_minimo.

3. Devuelva el diccionario resultante
"""

sucursal_1 = {
    "manzanas": 10,
    "peras": 5,
    "plátanos": 20
}

sucursal_2 = {
    "peras": 15,
    "naranjas": 8,
    "manzanas": 5
}

def fusionar_y_filtrar(inventario_a, inventario_b, umbral_minimo):
    inventario_final = {}

    # fusionando inventarios
    for inventario in (inventario_a, inventario_b):
        for producto, cantidad in inventario.items():
            inventario_final[producto] = inventario_final.get(producto, 0) + cantidad

    # filtrando datos
    for producto, cantidad in inventario_final.copy().items():
        if cantidad < umbral_minimo:
            inventario_final.pop(producto, None)
    
    return inventario_final

print(fusionar_y_filtrar(sucursal_1, sucursal_2, 20))
