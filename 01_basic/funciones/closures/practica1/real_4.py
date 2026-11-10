"""
Ejercicio 4: Logger con niveles de severidad configurables

Contexto: 

Los sistemas empresariales escriben registros de eventos (logs).
Dependiendo del entorno (producción o desarrollo), filtras qué tipo de mensajes
quieres ver (ej. solo errores críticos, o todo incluyendo información de depuración).

Descripción: 

Escribe una función fábrica crear_logger(nivel_minimo) donde el nivel de
severidad se pueda representar numéricamente (ej. 1 para INFO, 2 para
WARNING, 3 para ERROR). La función debe retornar un closure que reciba
(nivel_mensaje, mensaje). Si el nivel del mensaje es mayor o igual al nivel_minimo
configurado en la fábrica, debe imprimir o retornar el mensaje formateado; de lo
contrario, lo ignora.

Datos de entrada para probar:

Niveles: 1: INFO, 2: WARNING, 3: ERROR

log_produccion = crear_logger(2) (Solo
muestra WARNING o ERROR)

log_produccion(1, "Cargando usuario...")
-> No imprime nada (o retorna None)

log_produccion(3, "Conexión a base de
datos caída") -> Retorna/Imprime:
"[ERROR]: Conexión a base de datos
caída"
"""

def crear_logger(nivel_minimo: int):
    def generar_log(nivel_mensaje: int, mensaje: str):

        if nivel_mensaje >= nivel_minimo:
            mensaje_formateado = ""

            match nivel_mensaje:
                case 1: 
                    mensaje_formateado = f"[INFO]: {mensaje}"
                case 2:
                    mensaje_formateado = f"[WARNING]: {mensaje}"
                case 3:
                    mensaje_formateado = f"[ERROR]: {mensaje}"
                case _:
                    mensaje_formateado = f"[OTRO]: {mensaje}"

            return mensaje_formateado
        
        return None

    return generar_log

log_produccion = crear_logger(2)

print(log_produccion(1, "Cargando usuario..."))

print(log_produccion(3, "Conexión a base de datos caída"))
