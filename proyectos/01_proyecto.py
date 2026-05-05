# Examinador de tipo de datos - versión 1.0

def detection_type(value):
    try:
        return int(value), "int"
    except ValueError:
        try:
            return float(value), "float"
        except ValueError:
            if value.lower() in ["true", "false"]:
                # check logical operation (true or false), bool (tuple)
                return value.lower() == "true", "bool"
            
            if value == "None":
                return value, "NoneType"

            return value, "str"

value = input("Ingrese un valor: ")
result = detection_type(value)

print(f"Valor: {result[0]} - Tipo: {result[1]}")
