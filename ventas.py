ventas = [
    ("Carlos", 500),
    ("Juan", 300),
    ("Carlos", 200),
    ("María", 700),
    ("Juan", 100)
]

def total_ventas(ventas):

    contador = {}

    for venta in ventas:
        if venta in contador:
            contador[venta] += 1
        else:
            contador[venta] = 1

    return contador

res = total_ventas(ventas)

print(res)