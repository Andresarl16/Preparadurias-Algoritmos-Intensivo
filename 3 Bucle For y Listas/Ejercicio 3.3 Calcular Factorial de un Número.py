number = int(input("Introduzca número del que desea calcular el factorial: "))

factorial = 1

for i in range(2, number + 1):
    factorial *= i


print(f"El factorial de {number} es {factorial}")
