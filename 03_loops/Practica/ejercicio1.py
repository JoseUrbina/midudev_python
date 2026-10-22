"""
Tienes una lista con el estado de varios servicios de un servidor

- Recorre la lista con un bucle for
- Imprime "Servicio operativo" si el estado "ok"
- Imprime "Atención requerida" para cualquier otro estado
- Reto: Usa un operador ternario dentro del bucle para 
        decidir que texto imprimir

"""

estados = ["ok", "error", "ok", "warning", "ok", "error"]

for estado in estados:
    message = "Servicio operativo" if estado == "ok" else "Atención requerida"

    print(message)
