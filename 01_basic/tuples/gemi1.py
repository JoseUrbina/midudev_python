"""
Ejercicio 1: Formateador de coordenadas GPS 

En un sistema de entregas o delevery, las ubicaciones
se manejan como pares de coordenadas (latitud, longitud)
para asegurar que el punto no sea alterado por error
durante la ejecución del trayecto.

1. Crear una función formatear_ubicacion(coordenadas)
    que reciba una tupla (latitud, longitud)

2. La función debe desempaquetar (unpack) la tupla y retornar
    un retornar un string con el sig. formato:
    "Ubicación: [latitud]° N/S, [longitud]° E/W".

ej:
    coordenadas: (12.1328, -86.2504)
    salida: Ubicación: 12.1328° N/S, -86.2504° E/W
"""

def formatear_ubicacion(coordenadas: tuple) -> str:
    latitud, longitud = coordenadas

    return f"Ubicación: {latitud}° N/S, {longitud}° E/W"

coordenadas: tuple = (12.1328, -86.2504)

print(formatear_ubicacion(coordenadas))
