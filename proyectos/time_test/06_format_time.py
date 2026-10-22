# Prueba 1

import time

def obtener_horas(tiempo: float) -> int:
    return int(tiempo // 3600)

def obtener_minutos(tiempo: float) -> int:

    sobrante_horas = tiempo % 3600

    return int(sobrante_horas // 60)

def obtener_segundos(tiempo: float) -> float:
    return tiempo % 60

# FASE 5

inicio: float = time.time()
tiempo: float = 0

try:
    print("*** Cronometro digital ***")
    while True:

        final: float = time.time()

        resultado: float = final - inicio

        tiempo: float = round(resultado, 1)

        horas: int = obtener_horas(tiempo)
        minutos: int = obtener_minutos(tiempo)
        segundos: float = obtener_segundos(tiempo)

        print(f"Tiempo: {horas:02d}:{minutos:02d}:{segundos:04.1f}", end="\r")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nCronómetro detenido.")
    print(f"\nÚltimo tiempo {tiempo} seg")
