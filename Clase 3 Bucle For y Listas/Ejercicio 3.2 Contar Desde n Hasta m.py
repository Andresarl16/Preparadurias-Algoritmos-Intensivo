start = int(input("Introduzca el límite inferior para el conteo: "))
end = int(input("Introduzca el límite superior para el conteo: "))

print(f"El conteo desde {start} hasta {end} es:")

output = ""

for i in range(start, end+1):
    output += str(i) + ","

print(output)
