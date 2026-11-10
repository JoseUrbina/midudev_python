# A(B) -> C

def decorador(func):

    def wrapper(*args, **kwargs):
        print("Antes de la llamada a la función")
        resultado = func(*args, **kwargs)
        print("Despúes de la llamada a la función")

        return resultado

    return wrapper

@decorador
def hello_world(message):
    return f"{message} - fn original"

print(hello_world('Hello World, Welcome!'))
