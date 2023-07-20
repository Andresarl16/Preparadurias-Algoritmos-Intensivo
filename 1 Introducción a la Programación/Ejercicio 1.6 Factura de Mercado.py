price = float(input("Introduzca el valor del producto: "))
quantity = int(input("Introduzca la cantidad de dicho producto: "))

subtotal = price * quantity
iva = subtotal * 0.16
total = subtotal+iva

print(f"""
    Precio: {price}
    Cantidad: {quantity}
    Subtotal: {subtotal}
    IVA: {iva}
    Total: {total}
""")
