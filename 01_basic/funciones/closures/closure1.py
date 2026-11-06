'''
Ejercicio 1: El saludador personalizado

Propósito: 

Entender cómo una función interna (anidada) recuerda los
argumentos de la función externa incluso después de que 
esta última haya terminado de ejecutarse.

Descripción: 

Escribe una función fábrica llamada crear_saludador(saludo) 
que reciba una cadena de texto (ej. "Hola", "Buenos días") 
y devuelva una función interna. Esta función interna debe 
recibir un nombre (nombre) y retornar el saludo completo 
formateado (ej. "Hola, Carlos!").

Datos de entrada para probar:

Fábrica 1: 

saluda_hola =crear_saludador("Hola") -> Llamada:

saluda_hola("Ana") -> Resultado
esperado: "Hola, Ana!"

Fábrica 2: 
saluda_bienvenida = crear_saludador("Bienvenido a bordo")-> Llamada:
saluda_bienvenida("Marcos") -> Resultado esperado: "Bienvenido a bordo, Marcos!"
'''

from typing import Callable

def crear_saludador(saludo: str) -> Callable[[str], str]:

    def saludo_completo(nombre: str) -> str:
        return f"{saludo}, {nombre}!"

    return saludo_completo

saluda_hola = crear_saludador("Hola")
print(saluda_hola("Ana"))

saluda_bienvenida = crear_saludador("Bienvenido a bordo")
print(saluda_bienvenida("Marcos"))
