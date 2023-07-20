product_list = {
    "Leche": 2.50,
    "Pan": 1.50,
    "Huevos": 3.00,
    "Manzanas": 0.80,
    "Cereal": 4.50,
}

selected_product = input("Ingrese el producto que quiere revisar: ")

if selected_product in product_list:
    print(
        f"El producto {selected_product} si existe y su precio es: {product_list[selected_product]:.2f}"
    )
else:
    print(f"El producto {selected_product} NO existe")
