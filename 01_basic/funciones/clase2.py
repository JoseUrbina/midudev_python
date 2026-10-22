# Parametros

def count_to(number):
    for n in range(1, number + 1):
        print(n)

def multiply(number1, number2):
    resultado = number1 * number2
    print(f"El resultado de la operación es: {resultado}")

def full_name(first_name, last_name, prefix):
    full_name = f"{prefix} {first_name} {last_name}"
    print(full_name)

count_to(10)
multiply(10, 2)
full_name("José", "Urbina", "Mr.")
