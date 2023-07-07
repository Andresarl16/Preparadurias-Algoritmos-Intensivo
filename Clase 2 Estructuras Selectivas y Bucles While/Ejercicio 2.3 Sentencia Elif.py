first_number = int(input("Introduzca el primer número: "))
second_number = int(input("Introduzca el segundo número: "))

if (first_number > second_number):
    print(
        f"El primer número ({first_number}) es mayor que el segundo número ({second_number})")
elif (second_number > first_number):
    print(
        f"El segundo número ({second_number}) es mayor que el primer número ({first_number})")
else:
    print(
        f"El primer número ({first_number}) y el segundo número ({second_number}) son iguales")
