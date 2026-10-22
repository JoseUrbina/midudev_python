import time

print("Iniciando cuenta regresiva")

for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
else:
    print("¡FUEGO! BOOM...")

print(f"{'*'*20}")