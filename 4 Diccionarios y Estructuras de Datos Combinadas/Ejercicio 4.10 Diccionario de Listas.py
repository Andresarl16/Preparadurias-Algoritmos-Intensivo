phone_directory = {
    "Pedro": [345565, 265645, 654645],
    "Juan": [976545, 325464, 87654],
    "Andres": [267575, 645532, 6456765],
}

for person in phone_directory:
    phone_numbers = ""
    for number in phone_directory[person]:
        if phone_numbers != "":
            phone_numbers += ", " + str(number)
        else:
            phone_numbers += str(number)

    print(f"Los números de teléfono de {person} son ({phone_numbers})")
