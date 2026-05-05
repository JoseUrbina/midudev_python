# Examinador de tipos de datos - versión 2.0

import ast

def detection_type(value):
    # return : tuple (result, type_name)

    try:
        # ast.literal_eval(value) : convierte texto a objeto python
        # advantege : if value is code, it doesn't executed : error => return str
        # literal : son valores simples de python (números, strings,... dict, list, tuple, complex)

        result = ast.literal_eval(value)

        # type(value).__name__ : return data type name

        return result, type(result).__name__
    except (ValueError, SyntaxError):
        # case, it is not a valid literal, return str
        return value, "str"

# to get value
value = input("Ingrese un valor: ")

# call function detection_type, getting data
result = detection_type(value)

# print results
print(f"Valor: {result[0]} - Tipo: {result[1]}")
