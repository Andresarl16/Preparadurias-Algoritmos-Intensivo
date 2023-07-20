sentence = input("Introduzca una oración: ")
string = input("Introduzca la palabra que quiere contar: ")

print(
    f"La oración original es '{sentence}' y la palabra '{string}' aparece {sentence.count(string)} veces")
