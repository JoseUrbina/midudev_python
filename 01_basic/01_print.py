###
# 01-print()
# EL módulo print es el módulo que nos permite imprimir en consola
# Sirve para mostrar información en consola.
###

print("!Hola, mundo!")
print("!Bienvenidos a python!")
print('Esto también funciona con una comilla simple')

# Podemos agregar varios valores, separados por comas
# print() los mostrara separados por el separador por defecto " ", 
# sep = "value"  => se puede cambiar el valor por defecto del separador con el argumento sep
print("Python", "es", "genial")
print("Python", "es", "brutal", sep="-")

# print() : al final de cada llamada, agrega un salto de linea por defecto
# end = "value" => permite cambiar el valor por defecto del salto de linea con el argumento end
print("Esto se imprime", end=" ")
print("en la misma linea")

# Test: ejemplo del uso del print()

# recibe datos (input), las almacena en variables 
# y luego las muestra en consola con print()

message = input("Ingresa tu mensaje: ")
autor = input("Ingresa el nombre del creador del mensaje: ")

# Imprime el mensaje y el autor en consola, 
# utilizando diferentes maneras de mostrar la información con print().

print("Versión 1")
print("Mensaje:", message)
print(f"Creado por: {autor}")

# Mostrando un mensaje grande con f-strings y docstrings.
print(f"""Versión 2
    Mensaje: {message},
    Creado por: {autor}""")

# Cambiando el valor por defecto del separador con sep
print("Versión 3")
print("Mensaje:", message, sep="-")
print("Creado por", autor, sep=" @")

# Cambiando el valor por defecto del salto de linea con end
print("Versión 4")
print("Mensaje ingresado: ", end="")
print(message)
print("Creado por:", end=" ")
print(autor)
