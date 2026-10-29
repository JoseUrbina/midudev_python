"""
Ejercicio 1: Procesador de notificaciones 

Contexto: 
En un sistema backend, a menudo necesitamos enviar alertas a los
usuarios, pero el canal (correo, SMS, push) puede cambiar 
dinámicamente según la preferencia del usuario.

Reto: 
Crea una función llamada enviar_alerta que reciba el mensaje (un
string) y una función canal_envio (un callback). La función principal 
simplemente debe ejecutar el callback pasándole el mensaje.

Para practicar: 

Define dos callbacks sencillos (enviar_por_email, enviar_por_sms)
que impriman un mensaje simulando el envío, y pruébalos 
llamando a enviar_alerta.
"""

from typing import Callable

def enviar_por_email(mensaje: str) -> str:
    return f"Mensaje enviado por email: {mensaje}"

def enviar_por_sms(mensaje: str) -> str:
    return f"Mensaje enviado por sms: {mensaje}"

def enviar_alerta(mensaje: str, canal_envio: Callable[[str], str]) -> str:
    return canal_envio(mensaje)

print(enviar_alerta("Hello World !!!", enviar_por_email))
print(enviar_alerta("Hello World !!!", enviar_por_sms))
