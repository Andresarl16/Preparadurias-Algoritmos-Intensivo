limit = int(
    input("Introduzca el número entero positivo hasta el cual desea contar: "))

counter = 1

print(f"El conteo desde el 1 hasta el {limit} es:")

while (counter <= limit):
    print(counter)
    counter += 1
