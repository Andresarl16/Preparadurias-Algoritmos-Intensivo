number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dictionary = {}

for number in number_list:
    if number % 2 == 0:
        dictionary[number] = "PAR"
    else:
        dictionary[number] = "IMPAR"

for i in dictionary:
    print(f"El número {i} es {dictionary[i]}")
