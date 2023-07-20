number_1 = int(input("Introduzca el primer número: "))
number_2 = int(input("Introduzca el segundo número: "))

summation_1 = 1
dividers_1 = [1]
for i in range(2, number_1):
    if number_1 % i == 0:
        summation_1 += i
        dividers_1.append(i)

summation_2 = 1
dividers_2 = [1]
for i in range(2, number_2):
    if number_2 % i == 0:
        summation_2 += i
        dividers_2.append(i)

print(f"La lista de divisores de {number_1} es {dividers_1}")
print(f"La suma de la lista de divisores de {number_1} es {summation_1}")
print(f"La lista de divisores de {number_2} es {dividers_2}")
print(f"La suma de la lista de divisores de {number_2} es {summation_2}")
if summation_1 == number_2 and summation_2 == number_1:
    print(f"{number_1} y {number_2} son números amigos")
else:
    print(f"{number_1} y {number_2} no son números amigos")
