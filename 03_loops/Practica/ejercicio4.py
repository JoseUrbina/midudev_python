"""
- Tienes una lista de puntuaciones de un juego:
[45, 88, 92, 60, 30, 75, 100]

- Crea una nueva lista llamada resultados usando
    List comprehension en una sola línea de
    código

- La regla de conversión es: si la nota es
    >= 70, el valor debe ser "Aprobado", de
    contrario "Reprobado"
"""

puntuaciones = [45, 88, 92, 60, 30, 75, 100]

resultados = ["Aprobado" if puntuacion >= 70 else "Reprobado" for puntuacion in puntuaciones]

print(resultados)
