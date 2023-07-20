string = input("Introduzca una oración: ")

snake_case = string.lower().replace(" ", "_")

print(
    f"La oración original es '{string}' y la oración en snake case es '{snake_case}'")
