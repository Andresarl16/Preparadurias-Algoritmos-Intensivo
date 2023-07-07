limit = int(
    input("Introduzca el número entero positivo hasta el cual desea contar: "))

counter = 1
output = ""

print(f"El conteo desde el 1 hasta el {limit} es:")

while (counter <= limit):
    output += str(counter) + ","
    counter += 1

print(output)
