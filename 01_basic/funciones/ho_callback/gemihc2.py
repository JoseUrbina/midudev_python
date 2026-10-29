"""
Ejercicio 2: Sistema de filtrado y transformaciónde transacciones

Contexto: 
Trabajas en una pasarela de pagos. Tienes una lista de transacciones
bancarias y necesitas procesarlas aplicando reglas de negocio 
flexibles sin repetir código.

Reto: 

Escribe una función de orden superior llamada procesar_transacciones
que reciba una lista de diccionarios (cada uno con id, monto, estado, moneda) 
y una función de condición (callback) para filtrar cuáles procesar.

Para practicar: 

Haz que la función devuelva una nueva lista aplicando primero
el filtro del callback, y luego transformando el monto
(por ejemplo, aplicando un descuento o comisión) mediante 
otro callback opcional o anidado.
"""

transacciones = [
    {"id": 101, "monto": 150.0, "estado": "completado", "moneda": "USD"},
    {"id": 102, "monto": 45.5, "estado": "pendiente", "moneda": "USD"},
    {"id": 103, "monto": 300.0, "estado": "completado", "moneda": "EUR"},
    {"id": 104, "monto": 1200.0, "estado": "completado", "moneda": "USD"},
    {"id": 105, "monto": 80.0, "estado": "fallido", "moneda": "USD"},
    {"id": 106, "monto": 500.0, "estado": "completado", "moneda": "EUR"}
]

def es_completada(transacciones: list) -> list:
    return [t for t in transacciones if t["estado"] == "completado"]

def aplicar_comision(transaccion: dict):
    COMISION = 2.5

    transaccion["monto"] -= COMISION

    return transaccion


def procesar_transacciones(transacciones, condicion_filtro, transformador=None):

    transacciones_filtro = condicion_filtro(transacciones)

    if transformador:
        transacciones_transformadas = []

        for t in transacciones_filtro:
            transacciones_transformadas.append(aplicar_comision(t.copy()))

        return transacciones_transformadas
    
    return transacciones_filtro       

print(procesar_transacciones(transacciones, es_completada))
print(procesar_transacciones(transacciones, es_completada, aplicar_comision))
