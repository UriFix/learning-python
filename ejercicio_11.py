compras = [
    ("ana", "playera"),
    ("luis", "gorra"),
    ("ana", "playera"),
    ("luis", "playera"),
    ("marta", "gorra"),
    ("ana", "gorra"),
    ("luis", "gorra")
]

def clientes_distintos_por_producto(compras):
    pares_distintos = set(compras)
    resultado = {}
    for cliente, producto in pares_distintos:
        if producto in resultado:
            resultado[producto] += 1
        else:
            resultado[producto] = 1
    return resultado

print(clientes_distintos_por_producto(compras))

def producto_mas_clientes_distintos(compras):
    res = clientes_distintos_por_producto(compras)
    mayor = 0
    producto_mayor = ""
    for producto, cantidad in res.items():
        if cantidad > mayor:
            mayor = cantidad
            producto_mayor = producto

    return producto_mayor

print(producto_mas_clientes_distintos(compras))
        



