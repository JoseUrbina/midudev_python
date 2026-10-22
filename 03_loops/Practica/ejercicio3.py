"""
Nivel 3: Filtro e interrupción de bucles

Tienes un inventario de productos con sus precios.
Queremos procesar los productos uno a uno:

- Si el precio es menor a 20, asigna una etiqueta 
    "Económico". Si es 20 o más, asigna "Estándar".
    (Usa un ternario para la etiqueta)
- Imprime: "<Nombre>: <Etiqueta> ($<Precio>)".
- Regla especial: Si encuentras un producto de más de $1000,
    imprime un aviso de "Alerta de costo alto: <Nombre>" y
    rompe el bucle de inmediato(break)
"""

productos = [
    {"nombre": "Teclado", "precio": 50},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Mouse", "precio": 15},
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Cable HDMI", "precio": 10}
]

for producto in productos:
    precio = producto.get("precio", 0)
    nombre = producto.get("nombre", "Sin nombre")

    if precio > 1000:
        print(f"Alerta de costo alto: {nombre}")
        break

    etiqueta = "Estándar" if producto["precio"] >= 20 else "Económico"

    print(f"{nombre}: {etiqueta} (${precio})")
