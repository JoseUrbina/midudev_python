"""
Ejercicio 4: Búsqueda y anidamiento de datos

Dado un historial de transacciones bancarias estructurado
como una lista de diccionarios:

Escribe una función resumen_usuarios(transacciones) que devuelva
un diccionario anidado con el balance y detalle por usuario
con esta estructura.
""" 

transacciones = [
    {"usuario": "alice", "tipo": "deposito", "monto": 100},
    {"usuario": "bob", "tipo": "retiro", "monto": 50},
    {"usuario": "alice", "tipo": "retiro", "monto": 30},
    {"usuario": "alice", "tipo": "deposito", "monto": 50},
    {"usuario": "bob", "tipo": "deposito", "monto": 200}
]

def resumen_usuarios(transacciones):
    resumen = {}

    for transaccion in transacciones:
        usuario = transaccion.get("usuario")
        tipo = transaccion.get("tipo")
        monto = transaccion.get("monto")

        resumen[usuario] = resumen.get(usuario, {
                        "total_depositado": 0,
                        "total_retirado": 0,
                        "balance": 0
                        })

        if tipo == "deposito":
            resumen[usuario]["total_depositado"] += monto
            resumen[usuario]["balance"] += monto
        elif tipo == "retiro":
            resumen[usuario]["total_retirado"] += monto
            resumen[usuario]["balance"] -=  monto
    
    return resumen

print(resumen_usuarios(transacciones))
