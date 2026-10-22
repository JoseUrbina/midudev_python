"""
Ejercicio 1: Filtrado y limpieza de datos

Recibiste una lista de nombres desde un formulario web,
pero algunos campos están vacíos o tiene espacios
extra en los extremos.

Tarea:

1. Crea una lista llamada usuarios_limpios
2. Elimina los espacios en blanco de cada nombre con .strip().
3. Filtra la lista para ignorar las cadenas vacías
    o compuestas solo por espacios.
4. Muestra usuarios_limpios
"""

usuarios_raw = ["  Ana ", "Pedro", "", "   ", "MARIA  ", "   Carlos"]

# usuario_sin_espacio = [usuario.strip() for usuario in usuarios_raw]

usuarios_limpios = [usuario.strip() for usuario in usuarios_raw if usuario.strip()]

print(usuarios_limpios)
