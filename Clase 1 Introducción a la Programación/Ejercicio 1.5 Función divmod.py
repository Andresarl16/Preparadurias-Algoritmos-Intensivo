first_number = int(input("Ingrese el primer número: "))
second_number = int(input("Ingrese el segundo número: "))

quotient, remainder = divmod(first_number, second_number)

print(
    f"El cociente de la división de {first_number} entre {second_number} es {quotient} y su resto es {remainder}")
