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

complete_list = []

for number in numbers_1:
    if number not in complete_list:
        complete_list.append(number)

for number in numbers_2:
    if number not in complete_list:
        complete_list.append(number)

print(
    f"""
Los elementos de la lista 1 son {numbers_1}
Los elementos de la lista 2 son {numbers_2}
La unión de ambas listas sin repetidos es {complete_list}
"""
)
