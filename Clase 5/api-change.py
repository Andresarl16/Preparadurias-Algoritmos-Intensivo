api = [
    {
        "first_name": "Brynn",
        "second_name": "Roseby",
        "id": 14836003,
        "phone_number": "941-392-7190",
        "date_of_birth": "2001/10/26",
    },
    {
        "first_name": "Idaline",
        "second_name": "Fust",
        "id": 38680021,
        "phone_number": "832-128-3492",
        "date_of_birth": "1980/07/27",
    },
    {
        "first_name": "Carly",
        "second_name": "Guile",
        "id": 33822339,
        "phone_number": "788-919-9803",
        "date_of_birth": "1992/11/14",
    },
    {
        "first_name": "Galvin",
        "second_name": "Pickhaver",
        "id": 20141338,
        "phone_number": "170-233-8585",
        "date_of_birth": "2002/09/23",
    },
    {
        "first_name": "Brynna",
        "second_name": "Micka",
        "id": 16311071,
        "phone_number": "902-570-4768",
        "date_of_birth": "1980/05/18",
    },
    {
        "first_name": "Guglielmo",
        "second_name": "Stammers",
        "id": 36300264,
        "phone_number": "345-540-2217",
        "date_of_birth": "1996/12/02",
    },
    {
        "first_name": "Catie",
        "second_name": "Cornock",
        "id": 30105606,
        "phone_number": "320-467-0760",
        "date_of_birth": "2000/01/06",
    },
    {
        "first_name": "Bride",
        "second_name": "Nibloe",
        "id": 14240668,
        "phone_number": "903-296-0306",
        "date_of_birth": "1993/09/02",
    },
    {
        "first_name": "Daria",
        "second_name": "Jankiewicz",
        "id": 13031787,
        "phone_number": "420-342-4466",
        "date_of_birth": "2002/12/16",
    },
    {
        "first_name": "Shamus",
        "second_name": "MacGowan",
        "id": 31637624,
        "phone_number": "433-654-9825",
        "date_of_birth": "1989/10/31",
    },
    {
        "first_name": "Cristy",
        "second_name": "Darrington",
        "id": 13023069,
        "phone_number": "915-304-9624",
        "date_of_birth": "1999/03/25",
    },
    {
        "first_name": "Shannan",
        "second_name": "Goody",
        "id": 30483626,
        "phone_number": "424-578-8164",
        "date_of_birth": "1996/04/23",
    },
    {
        "first_name": "Arlyn",
        "second_name": "Thomann",
        "id": 14948939,
        "phone_number": "320-773-8675",
        "date_of_birth": "1998/04/23",
    },
    {
        "first_name": "Marcellina",
        "second_name": "Shalloe",
        "id": 19992912,
        "phone_number": "177-314-2098",
        "date_of_birth": "1980/01/31",
    },
    {
        "first_name": "Giffard",
        "second_name": "Lesley",
        "id": 17825393,
        "phone_number": "214-567-1249",
        "date_of_birth": "1997/03/31",
    },
    {
        "first_name": "Candida",
        "second_name": "Giacomini",
        "id": 10158017,
        "phone_number": "388-717-4141",
        "date_of_birth": "2001/04/01",
    },
    {
        "first_name": "Cammy",
        "second_name": "Sutherington",
        "id": 14366897,
        "phone_number": "117-463-9838",
        "date_of_birth": "1998/12/02",
    },
    {
        "first_name": "Jeffry",
        "second_name": "Bazylets",
        "id": 27226255,
        "phone_number": "693-388-9019",
        "date_of_birth": "1999/05/16",
    },
    {
        "first_name": "Paulita",
        "second_name": "Rosas",
        "id": 17970510,
        "phone_number": "436-255-3357",
        "date_of_birth": "1998/02/24",
    },
    {
        "first_name": "Blake",
        "second_name": "Tadd",
        "id": 33805101,
        "phone_number": "415-410-1159",
        "date_of_birth": "2004/03/15",
    },
    {
        "first_name": "Anallise",
        "second_name": "Einchcombe",
        "id": 37366684,
        "phone_number": "356-401-3270",
        "date_of_birth": "1998/09/27",
    },
    {
        "first_name": "Hayden",
        "second_name": "Gimber",
        "id": 25802196,
        "phone_number": "891-737-5509",
        "date_of_birth": "1997/11/02",
    },
]

from random import randrange


def generate_random_phone_number(start):
    return f"{start}{randrange(100, 999)}-{randrange(1000, 9999)}"


for student in api:
    student["phone_number"] = [
        student["phone_number"],
        generate_random_phone_number(student["phone_number"][0:4]),
        generate_random_phone_number(student["phone_number"][0:4]),
    ]

print(api)
