compras = [
    ("ana", "playera"),
    ("luis", "gorra"),
    ("ana", "gorra"),
    ("ana", "playera"),
    ("luis", "pantalon")
]

def historial_por_cliente(compras):
    resultado = {}
    
    for cliente, producto in compras:
        if cliente in resultado:
            resultado[cliente].append(producto)
        else:
            resultado[cliente] = [producto]
            
            
    return resultado

print(historial_por_cliente(compras))