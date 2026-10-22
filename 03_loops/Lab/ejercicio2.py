"""
Define una variable de tipo string llamada sentence.
Utilizando un ciclo while, imprime la cantidad de
caracteres que posee la variable hasta encontrar un punto (.).
"""

sentence = "Hola mundo. Curso de Python."

i = 0
contador = 0

while i <= len(sentence):
    if sentence[i] == ".":
        break

    contador += 1
    i += 1

print(contador)
