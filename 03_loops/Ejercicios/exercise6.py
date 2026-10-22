# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

# Determinando solo si el número ingresado es primo

# if n <= 1:
#     print(f"El número {n} no es primo")
# else:
#     es_primo = True
#     divisor = 2

#     while divisor * divisor <= n:
#         if n % divisor == 0:
#             es_primo = False
#             break

#         divisor += 1

#     print(f"¿Es primo? : {es_primo}")

if n <= 1:
    print(f"El número {n} no es primo")
else:
    # inicializar la variable en 2 := primo: numeros enteros > 1
    numero = 2

    # 1er ciclo: recorrer 1 a 1 hasta llegar a n
    while numero <= n:
        es_primo = True # Asumir que el número es primo hasta demostrar lo contrario
        divisor = 2 # 

        # ciclo interno: recorre 1 a 1 hasta el valor actual evaluado en el ciclo principal
        # divisor * divisor := optimización (evaluar hasta el numero  el sqrt(numero) 
        # =|= (el numero se divide en 2 si en un lado ))
        while divisor * divisor <= numero:
            if numero % divisor == 0:
                es_primo = False
                break

            divisor += 1

        if es_primo:
            print(numero)
        
        numero += 1
