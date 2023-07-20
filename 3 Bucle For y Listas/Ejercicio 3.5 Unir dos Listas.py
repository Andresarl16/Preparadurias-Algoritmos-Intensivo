numbers_1 = []
numbers_2 = []

i = 1
while True:
    numbers_1.append(int(input(f"Introduzca el número {i} de la lista 1: ")))
    option = int(
        input(
            "Si desea ingresar otro número a la lista introduzca 1, para terminar introuzca 0: "
        )
    )
    if option == 0:
        break

    i += 1

i = 1
while True:
    numbers_2.append(int(input(f"Introduzca el número {i} de la lista 2: ")))
    option = int(
        input(
            "Si desea ingresar otro número a la lista introduzca 1, para terminar introuzca 0: "
        )
    )
    if option == 0:
        break

    i += 1

complete_list = numbers_1 + numbers_2

print(
    f"""
Los elementos de la lista 1 son {numbers_1}
Los elementos de la lista 2 son {numbers_2}
La unión de ambas listas es {complete_list}
"""
)
