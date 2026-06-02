###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinamico y de tipado fuerte
###

# Asignar una variable
my_name = "sparrow"

print(my_name)


# Reasignar valores a variables en tiempo de ejecución

age = 32
print(age)

age = 40
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# no tienes que declararlo explicitamente

name = "midudev"
print(type(name))

# name = 32
# print(type(name))

# Tipado fuerte: python no realiza conversiones de tipo automatica

#  print(10 + "2") -> error: tipado fuerte

# f- string : literal de cadena de formato
print(f"Hola {my_name}, tengo {age + 4} años")

# no recomendada forma de asignar variables

name, age, city = "midu", 45, "Bogotá"

print(name, age, city, sep = " - ")

# Convenciones de nombres de variables

mi_nombre_de_variable = "helloworld" # snake_case

job = "carpenter" # one word

number_1 = 23 # with numbers at the end

# Todas mayúsculas : CONSTANTES EN PYTHON POR CONVENCIÓN
# no existen las constantes en python

# constante: es un valor que no cambia
MI_CONSTANTE = 3.1416 # UPPER_CASE -> constante

# No es nombre válido usar palabras reservadas como nombre de variables

# True = False -> error

### Tratando de convertir python con tipado dinamico a tipado estatico

# Anotaciones de tipos : sirve para mostrar que tipo es la variable
# python en tiempo de ejecución se salta las anotaciones, no las toma en cuenta


# Opción 1: vs code : configuración del editor, edit typecheck -> python
# EL editor muestra el error con las anotaciones, pero siempre
# python no las toma en cuenta en tiempo de ejecución

is_user_logged_in : bool = True
print(is_user_logged_in)

# is_user_logged_in = 24
# print(is_user_logged_in)

# vs code: válida los tipos en todo el file, no importa el
# lugar donde fue establecida la anotación
name : str = "peter parker"
