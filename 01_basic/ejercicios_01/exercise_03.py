
import os

os.system("clear" if os.name == "posix" else "cls")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

print(f"{'-'*10}")

cadena = "12345"
numero_entero = int(cadena)
numero_flotante = float(cadena)

print(f"Número entero: {numero_entero}")
print(f"Número como flotante: {numero_flotante}")

print(f"{'-'*10}")

entero = int(3.99)
print(f"3.99 convertido a entero: {entero}")
