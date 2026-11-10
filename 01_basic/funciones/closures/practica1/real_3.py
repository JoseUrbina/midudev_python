"""
Ejercicio 3: Control de velocidad o Rate Limiter

Contexto: 

En APIs públicas o sistemas de login, se implementa una política de Rate
Limiting para evitar ataques de fuerza bruta o saturación, limitando 
cuántas peticiones puede hacer un usuario en un rango de tiempo o número 
de intentos antes de bloquearlo temporalmente.

Descripción: 

Crea una función crear_limitador_tasa(max_llamadas) que reciba el límite
de peticiones permitidas. La clausura debe retornar una función que
acepte una acción (simulada por un texto o número). Si el número de llamadas
realizadas no supera el límite, incrementa el contador y retorna True (Permitido). Si ya
alcanzó o superó el límite, debe retornar False (Bloqueado/Demasiadas solicitudes).
Añade una función hermana o un mecanismo interno si deseas reiniciar elcontador 
(opcional, con que maneje el bloqueo basta).

Datos de entrada para probar:

llamar_api = crear_limitador_tasa(3)
llamar_api() -> True (Petición 1)
llamar_api() -> True (Petición 2)
llamar_api() -> True (Petición 3)
llamar_api() -> False (Límite excedido)
"""

def crear_limitador_tasa(max_llamadas: int):
    contador = 0

    def limitar(accion=None):
        nonlocal contador

        if contador >= max_llamadas:
            return False

        contador += 1
        return True

    def reiniciar_contador():
        nonlocal contador

        contador = 0
        return f"Se reinicio el contador a {contador} de {max_llamadas} llamadas."

    return limitar, reiniciar_contador

llamar_api, reiniciar_conteo = crear_limitador_tasa(4)

print(llamar_api())
print(llamar_api())
print(llamar_api())
print(llamar_api())
print(llamar_api())

print(reiniciar_conteo())
print(llamar_api())
