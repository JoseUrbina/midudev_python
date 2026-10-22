import time

limite = 10
tiempo = 0
inicio = time.time()

while tiempo < 10:
    final = time.time()

    resultado = final - inicio

    tiempo = round(resultado, 2)

    print(f"Tiempo: {tiempo}")

    time.sleep(0.1)
else:
    print("¡Tiempo terminado!")