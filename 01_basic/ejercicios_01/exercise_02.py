
import os

os.system("clear" if os.name == "posix" else "cls")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"{'-'*10}")

print(f"a: {type(a)}")
print(f"b: {type(b)}")
print(f"c: {type(c)}")
print(f"d: {type(d)}")
print(f"e: {type(e)}")

print(f"{'-'*10}")
