"""
Ejercicio 1: Limpieza de datos en una API

Estás recibiendo una lista de nombres de usuarios desde un frontend,
pero vienen con espacios de más y desordenados. Tienes que 
limpiarlos antes de guardarlos en la base de datos.

Tarea:

Crea una función lambda que tome un string con espacios al inicio y al final,
y lo convierta en formato titulo. Luego aplicala a toda una lista usando map
"""

usuarios_sucios = ["  carlos mendoza ", "ana gomez", "  LUIS TORRES  ", "maria perez "]

limpieza_datos = lambda nombre: " ".join([n.capitalize() for n in nombre.strip().lower().split(" ")])

usuarios_limpios = list(map(limpieza_datos, usuarios_sucios))

print(usuarios_limpios)
