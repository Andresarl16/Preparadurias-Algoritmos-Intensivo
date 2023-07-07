string = input("Introduzca una oración: ")
sub_string = input(
    "Introduzca los caracteres que quiere convertir a mayúsculas: ")

print(f"""
La oración original es '{string}'
La secuencia de caracteres a convertir a mayúsculas es '{sub_string}'
La oración transformada es '{string.replace(sub_string, sub_string.upper())}'
""")
