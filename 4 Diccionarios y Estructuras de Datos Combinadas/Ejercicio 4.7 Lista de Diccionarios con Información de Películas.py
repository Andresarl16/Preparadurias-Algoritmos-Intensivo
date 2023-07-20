movie_list = [
    {"title": "El Padrino", "director": "Francis Ford Coppola", "year": 1972},
    {"title": "Parásitos", "director": "Bong Joon-ho", "year": 2019},
    {"title": "El viaje de Chihiro", "director": "Hayao Miyazaki", "year": 2001},
]

for movie in movie_list:
    print(
        f"Título: [{movie['title']}] - Director: [{movie['director']}] - Año: [{movie['year']}]"
    )
