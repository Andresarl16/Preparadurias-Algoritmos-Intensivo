car_list = [
    {"brand": "Chevrolet", "model": "Spark GT", "price": 39990},
    {"brand": "Renault", "model": "Kwid", "price": 37990},
    {"brand": "Kia", "model": "Picanto", "price": 43990},
    {"brand": "Suzuki", "model": "Swift", "price": 49990},
]

for car in car_list:
    car["price"] += 500

for car in car_list:
    print(
        f"El carro de marca {car['brand']} y modelo {car['model']} tiene un precio de: {car['price']}"
    )
