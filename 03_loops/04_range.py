###
# función range()
#  Permite crear una secuencia de números, que se va creando 1*1 conforme se necesita.
###

print("Range():")

nums = range(5)

print(nums)
print(type(nums))

# generando una secuencia de números del 0 - 9
for i in range(10):
    print(i)

# range(inicio, fin(excluido))
for i in range(5, 10 + 1):
    print(i)

# range(inicio, fin (excluido), paso)
for n in range(1, 10 + 1, 2):
    print(n)

# contador en reversa
for n in range(10, 0, -1):
    print(n)

# range() con números negativos
for i in range(-4, 0):
    print(i)

# range() -> repitiendo acciones
for _ in range(3):
    print("Hello world!")

# convirtiendo range() to list()
numeros = range(10)
list_of_nums = list(numeros)
print(list_of_nums)
print(type(list_of_nums))
