precios = {"playera": 200, "gorra": 150, "pantalon": 400}

pedidos = [
    ("ana", "playera", 2),
    ("luis", "gorra", 1),
    ("ana", "pantalon", 1),
    ("luis", "playera", 3),
    ("marta", "gorra", 2)
]

def total_por_cliente(pedidos, precios):
    totales = {}
    
    for cliente, producto, cantidad in pedidos:
        precio = precios[producto]
        monto = precio * cantidad
        if cliente in totales:
            totales[cliente] += monto
        else:
            totales[cliente] = monto
            
    return totales
    
print(total_por_cliente(pedidos, precios))