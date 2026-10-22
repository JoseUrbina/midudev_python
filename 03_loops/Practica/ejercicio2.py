"""
Nivel 2: Clasificador de Usuarios

Tienes una lista de edades:
- Recorre la lista de edades
- Usar operador ternario para determinar si la persona >= 18
- Guarda los resultados en una nueva lista llama categorias
- Muestra la lista final categorias
"""

edades = [12, 25, 17, 40, 15, 65, 8]

# Forma 1

# categorias = []

# for edad in edades:
#     resultado = "Mayor de edad" if edad >= 18 else "Menor de edad"

#     categorias.append(resultado)

# Forma 2

categorias = ["Mayor de edad" if edad >= 18 else "Menor de edad" for edad in edades]

print(categorias)
