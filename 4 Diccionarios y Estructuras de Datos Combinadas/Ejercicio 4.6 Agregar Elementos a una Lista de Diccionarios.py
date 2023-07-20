contact_list = []

for i in range(1, 4):
    name = input(f"Ingrese el nombre del {i}° contacto: ")
    phone_number = input(f"Ingrese el número de teléfono del {i}° contacto: ")

    contact_list.append({"name": name, "phone_number": phone_number})

for contact in contact_list:
    print(f"El número de {contact['name']} es {contact['phone_number']}")
