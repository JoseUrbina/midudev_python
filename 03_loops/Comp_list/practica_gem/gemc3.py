"""
Ejercicio 3: LIst comprehension anidada/matrices

Trabajas con una matriz 2D que representa las ventas
de un equipo por trimentre (c/sublista es un vendedor)

Tarea:

1. Crea una sola lista plana(1D) llamada todas_las_ventas
    usando una sola list comprehension anidada.
2. Además, filtra para que en esa lista plana solo entren
    los valores mayores o iguales a 200.
3. Muestra todas_las_ventas.
"""

ventas_trimestrales = [
    [100, 250, 300], # Vendedor 1
    [400, 150, 500], # Vendedor 2
    [50, 80, 120]    # Vendedor 3
]

todas_las_ventas = [venta for ventas_vendedor in ventas_trimestrales for venta in ventas_vendedor if venta >= 200]

print(todas_las_ventas)
