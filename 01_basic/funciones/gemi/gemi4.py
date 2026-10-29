"""
Ejercicio 4: Generador de funciones de descuento dinámicas

Estás diseñando el módulo de promociones de una pasarela de pago.
Dependiendo de la temporada, el sistema necesita generar funciones matemáticas
de descuento personalizadas al vuelo.

Tarea:

Escribe una función normal llamada crear_descuento(porcentaje)
que retorne una función lambda capaz de calcular el precio final
aplicando dicho descuento. Pruébala generando un descuento
del 15% y aplicandoselo a varios precios.
"""

def crear_descuento(porcentaje):
    return lambda precio: precio * (1 - (porcentaje/100))

descuento_navidad = crear_descuento(15)

print(descuento_navidad(100))
print(descuento_navidad(200))
