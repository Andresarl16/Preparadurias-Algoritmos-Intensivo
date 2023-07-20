product_list = [
    {"name": "Pan", "price": 2.20, "stock": 15},
    {"name": "Azúcar", "price": 3.15, "stock": 23},
    {"name": "Queso", "price": 2.87, "stock": 8},
]

selected_product = input("Ingrese el producto que desea buscar: ")

found_product = None
for product in product_list:
    if product["name"] == selected_product:
        found_product = product
        break

if found_product:
    print(f"El producto {selected_product} se encuentra en la lista de productos")
    print(
        f"Su precio es de {found_product['price']} y su stock es de {found_product['stock']}"
    )
else:
    print(f"El producto {selected_product} NO se encuentra en la lista de productos")
