"""
Ejercicio 3: Estructuración de registros de base de datos

Cuando haces consultas a bases de datos en Python usando conectores
nativos (como sqlite3 o psycopg2), los resultados suelen retornar
como una lista de tuplas, donde c/tupla representa una fila/registro.

Objetivo:

Dado un reporte de ventas sin procesar:

1. Escribe una función obtener_resumen_ventas(ventas)
    que iterará sobre esta estructura.

2. Suma el total de ingresos.

3. Retorna una tupla de 2 elementos (total_ingresos, cantidad_transacciones)
"""

ventas = [
    ("2026-10-01", "Laptop", 1200.00),
    ("2026-10-01", "Mouse", 25.50),
    ("2026-10-02", "Teclado", 45.00),
    ("2026-10-02", "Monitor", 300.00)
]

def obtener_resumen_ventas(ventas: list):
    total_ingresos: float = 0
    cantidad_transacciones: int = len(ventas)

    for venta in ventas:
        total_ingresos += venta[2]

    return total_ingresos, cantidad_transacciones

total_ingresos, cantidad_transacciones = obtener_resumen_ventas(ventas)

print(f"Total de ingresos: {total_ingresos}")
print(f"Cantidad de transacciones: {cantidad_transacciones}")
