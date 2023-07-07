while True:
    number = int(input("Introduzca el primer número: "))

    if (number % 2 == 0):
        print(f"El número {number} es par")
    else:
        print(f"El número {number} es impar")

    finish = int(
        input("¿Quiere realizar otra comprobación?\n0 -> Terminar\n1 -> Continuar\n"))

    if (finish == 0):
        break

print("La ejecución a finalizado")
