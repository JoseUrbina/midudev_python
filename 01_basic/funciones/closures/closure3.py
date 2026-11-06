"""
Ejercicio 3: Control de intentos

Propósito:
Simular un estado privado que se actualiza y se bloquea al alcanzar un
límite, ideal para lógica de seguridad o validaciones.

Descripción:
Crea una función crear_validador_pin(pin_correcto, max_intentos) 
que reciba el PIN válido y un límite de intentos fallidos permitidos.
La clausura debe retornar una función que acepte un PIN ingresado. 
Si el PIN coincide, retorna True. Si falla, reduce el
contador de intentos y retorna False. Si se superan los intentos 
máximos permitidos, debe retornar "Bloqueado" en cualquier
intento posterior.

Datos de entrada para probar:

validar = crear_validador_pin("1234", 2)

Llamada 1: validar("0000") -> False
(Quedan 1 intento)

Llamada 2: validar("9999") -> False
(Agotados los intentos)

Llamada 3: validar("1234") ->
"Bloqueado" (Ya no se puede verificar aunque el PIN sea correcto)
"""

def crear_validador_pin(pin_correcto: str, max_intentos: int):
    contador = 0

    def validar_pin(pin: str):
        nonlocal contador

        if contador < max_intentos:
            if pin == pin_correcto:
                return True
            else:
                contador += 1
                return False
        else:
            return "Bloqueado"

    return validar_pin

validar = crear_validador_pin("1234", 2)

print(f"Validador PIN: {validar("0000")}")
print(f"Validador PIN: {validar("9999")}")
print(f"Validador PIN: {validar("1234")}")
