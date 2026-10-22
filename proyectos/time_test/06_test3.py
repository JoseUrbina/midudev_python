import time

inicio = time.time()

while True:
    final = time.time()

    resultado = final - inicio

    print(f"{resultado}")

    if int(resultado) == 10:
        break
