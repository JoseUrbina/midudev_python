options = {
    "s": lambda number1, number2: number1 + number2,
    "r": lambda number1, number2: number1 - number2,
    "m": lambda number1, number2: number1 * number2,
    "d": lambda number1, number2: number1 / number2
}

option = input("Ingrese la operación a realizar (s, r, m, d): ")

number1 = int(input("Ingrese el primer valor: "))
number2 = int(input("Ingrese el segundo valor: "))

default = lambda *args, **kwargs: "Lo sentimos, operación no válida."

function = options.get(option, default)

try:
    total = function(number1, number2)

    print(total)
except ZeroDivisionError:
    print("Error, no se puede dividir por 0.")
