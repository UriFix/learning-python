precios = {"playera": 200, "gorra": 150, "pantalon": 400}

pedidos = [
    ("ana", "playera", 2),
    ("luis", "gorra", 1),
    ("ana", "pantalon", 1),
    ("luis", "playera", 3),
    ("marta", "gorra", 2)
]

def total_por_cliente(pedidos, precios):
    print