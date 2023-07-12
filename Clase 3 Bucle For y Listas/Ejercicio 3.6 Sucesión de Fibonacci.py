limit = int(
    input("Introduzca la cantidad de números de la sucesión que quiere ver: "))

num1 = 0
num2 = 1
num3 = 1

succession = [0, 1]

for i in range(1, limit):
    num3 = num1 + num2
    succession.append(num3)

    num1 = num2
    num2 = num3

print(f"Los {limit} primeros números de la sucesión son: {succession}")
