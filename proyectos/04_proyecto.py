"""
    Has consumido X cantidad de megas en
    wikipedia, y Y cantidad de megas en memes.
    El costo de visitar wikipedia es de $0.10
    y el de los memes es de $0.05.

    Si el total consumido es mayor a $100
    imprime "Consumo demasiado alto", si
    el consumo de ver memes es mayor al de leer wikipedia
    imprime: "Wow, muchos memes".
"""

def calcular_costo_wikipedia(megas: float) -> float:
    return megas * 0.10

def calcular_costo_memes(megas: float) -> float:
    return megas * 0.05

megas_wikipedia = float(input("Ingrese la cantidad de megas consumidos en Wikipedia: "))
megas_memes = float(input("Ingrese la cantidad de megas consumidos en memes: "))

consumo_wikipedia = calcular_costo_wikipedia(megas_wikipedia)
consumo_memes = calcular_costo_memes(megas_memes)

total_consumo = consumo_wikipedia + consumo_memes

# 1er validación: consumo total
if total_consumo > 100:
    print("Consumo demasiado alto")

# 2da validación: consumo de memes vs wikipedia
if consumo_memes > consumo_wikipedia:
    print("Wow, muchos memes")
