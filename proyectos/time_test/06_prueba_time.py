# Prueba 1

import time

# FASE 5

inicio = time.time()
tiempo = 0

try:
    while True:
        final = time.time()

        resultado = final - inicio

        tiempo = round(resultado, 1)

        print(f"Tiempo: {tiempo} seg", end="\r")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nCronómetro detenido.")
    print(f"\nÚltimo tiempo {tiempo} seg")
