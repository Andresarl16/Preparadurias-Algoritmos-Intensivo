number = int(input("Introduzca el número que quiere comprobar: "))

isPrime = True
dividers = [1]
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        dividers.append(i)

dividers.append(number)

print(f"La lista de divisores de {number} es {dividers}")
if isPrime:
    print(f"El número {number} es primo")
else:
    print(f"El número {number} no es primo")
