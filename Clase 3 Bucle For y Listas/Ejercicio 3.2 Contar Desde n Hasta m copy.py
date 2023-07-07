number = int(input("Introduzca un número: "))


prime = True
dividers = [1]
for i in range(2, number):
    if (number % i == 0):
        dividers.append(i)
        prime = False

if (number != 1):
    dividers.append(number)

print(f"Los divisores del número son: {dividers}")

if (prime):
    print("El número es primo")
else:
    print("El número no primo")
