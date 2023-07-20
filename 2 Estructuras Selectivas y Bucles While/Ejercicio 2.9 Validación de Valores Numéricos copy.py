while True:
    word = input("Introduzca una palabra: ")

    if word.isalpha():
        break

    print("Valor inválido")


print("¡Valor válido!")
