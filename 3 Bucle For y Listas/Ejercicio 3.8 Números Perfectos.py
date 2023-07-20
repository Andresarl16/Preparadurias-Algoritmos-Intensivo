number = int(input("Introduzca el número que quiere comprobar: "))

summation = 1
dividers = [1]
for i in range(2, number):
    if number % i == 0:
        summation += i
        dividers.append(i)

print(f"La lista de divisores de {number} es {dividers}")
print(f"La suma de la lista de divisores es {summation}")
if number == summation:
    print("Por lo que el número es perfecto")
else:
    print("Por lo que el número no es perfecto")
