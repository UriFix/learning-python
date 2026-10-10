inventario = [
    ("playera", 10),
    ("pantalon", 5),
    ("gorra", 8),
    ("playera", 3),
    ("gorra", 2),
    ("pantalon", 4)
]

def stock_total(inventario):
    contador = {}

    for producto, cantidad in inventario:
        if producto in contador:
            contador[producto] += cantidad
        else:
            contador[producto] = cantidad
    return contador

res = stock_total(inventario)

print(res)

