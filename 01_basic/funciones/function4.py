# Funciones como ciudadanos de primera clase

def deposit(balance: int, amount=0) -> int:
    return balance + amount

def withdraw(balance: int, amount=0) -> int:
    if amount > balance:
        return None
    return balance - amount

# def default(*args, **kwargs):
#     return "Lo sentimos, operación NO válida."    

# variable = function (sin parentesis porque queremos la función, 
#                       los parentesis ejecutan la función y obtenemos un resultado)

"""
func1 = deposit
func2 = withdraw

print(func1(100, 10))
print(func2(100, 20))
"""

options = {
    'a': deposit,
    'b': withdraw
}

option = input("Ingrese la operación a realizar (a/b): ")
balance = int(input("Ingrese su balance: "))
amount = int(input("Ingrese la cantidad: "))

default = lambda *args, **kwargs: "Lo sentimos, operación NO válida."

function = options.get(option, default)

print(function(balance, amount))
