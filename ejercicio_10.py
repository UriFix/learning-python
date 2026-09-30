compras = [
    ("ana", "playera"),
    ("luis", "gorra"),
    ("ana", "playera"),
    ("luis", "playera"),
    ("marta", "gorra"),
    ("ana", "gorra"),
    ("luis", "gorra")
]


def clientes_por_producto(compras):
    resultado = {}

    for cliente, producto in compras:
        if producto in resultado:
            # producto ya existe: ¿qué haces con su set?
            resultado[producto].add(cliente)
        else:
            # producto nuevo: ¿qué guardas?
            clientes = set()    
            clientes.add(cliente)
            resultado[producto] = clientes

    return resultado

print(clientes_por_producto(compras))


