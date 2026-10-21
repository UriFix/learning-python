precios = {"playera": 200, "gorra": 150, "pantalon": 400}

pedidos = [
    ("ana", "playera", 2),
    ("luis", "gorra", 1),
    ("ana", "calcetin", 1)
]

def total_por_cliente(pedidos, precios):
    totales = {}

    for cliente, producto, cantidad in pedidos:
        try:
            precio = precios[producto]
        except KeyError:
            print(f"no hay precio para {producto}")
            continue                      # <- aquí va la palabra que corta la vuelta
        monto = precio * cantidad
        if cliente in totales:
            totales[cliente] += monto
        else:
            totales[cliente] = monto

    return totales

print(total_por_cliente(pedidos, precios))