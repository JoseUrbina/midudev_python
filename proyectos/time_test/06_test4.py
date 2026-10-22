import time

inicio = time.time()

while True:
    final = time.time()

    resultado = final - inicio

    tiempo = round(resultado, 2)

    print(f"Tiempo: {tiempo}")

    time.sleep(0.1)
