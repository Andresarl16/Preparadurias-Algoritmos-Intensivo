numbers = []

for i in range(1, 6):
    numbers.append(int(input(f"Introduzca el {i} número: ")))


total = sum(numbers)

print(f"La suma de los números {numbers} es: {total}")
