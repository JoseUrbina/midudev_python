
import os

os.system("clear" if os.name == "posix" else "cls")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

print(f"{'-'*10}")

nombre = "José"
edad = 33
altura = 1.56

print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

print(f"{'-'*10}")
