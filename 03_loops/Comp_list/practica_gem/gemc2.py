"""
Ejercicio 2: Filtrado + transformación con diccionarios

Tienes una lista de transacciones bancarias. Quieres 
identificar únicamente los retiros de dinero (montos negativos)
e ignorar los depositos.

Tarea:

- Crea una lista llamada retiros_formateados.
- Filtra únicamente los montos menores a 0.
- Transforma esos valores para convertirlos
    en montos positivos y formatea c/u como un
    string con el simbolo $. ej. $45.5
- Muestra la lista final
"""

transacciones = [150.0, -45.5, 200.0, -120.0, -15.0, 500.0, -8.99]

retiros_formateados = [f"${abs(monto)}" for monto in transacciones if monto < 0]

print(retiros_formateados)
