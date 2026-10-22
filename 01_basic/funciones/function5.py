"""
Lambda function : función anonima o sin nombre. <body> (una sola línea de código)

lambda <parametros>: <body> Siempre retornan un valor.
"""

# add = lambda number1, number2=0: number1 + number2

add = lambda *args: sum(args)

print(add(10))
print(add(10, 20, 30, 40, 50, 60, 70))
