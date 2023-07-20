weight = float(input("Introduzca su peso: "))
height = float(input("Introduzca su altura: "))
bmi_value = weight / (height ** 2)

print(
    f"Dado tu peso de {weight:.2f} y tu altura de {height:.2f}, tu imc es {bmi_value:.2f}")
