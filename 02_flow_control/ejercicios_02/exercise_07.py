# Verificar si una texto es palindroma

import os
os.system("clear" if os.name == "posix" else "cls")

texto = input("Ingrese su texto: ")

# delete blank space, to compare the word : palindromo
nospace_word = texto.replace(" ", "")

if nospace_word.lower() == nospace_word[::-1].lower():
    print(f"Texto ({texto}) es palindroma")
else:
    print(f"Texto ({texto}) no es palindroma")
