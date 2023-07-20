section_list = [
    ["Pedro", "Jose", "Ana", "Valeria"],
    ["Juan", "Laura", "Daniela", "Federico"],
]

i = 1
for section in section_list:
    students_output = ""
    for student in section:
        if students_output != "":
            students_output += ", " + student
        else:
            students_output += student

    print(f"Los estudiantes de la sección {i} son: {students_output}")
    i += 1
