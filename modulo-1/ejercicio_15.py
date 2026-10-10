compras = [
    ("ana", "playera"),
    ("luis", "gorra"),
    ("ana", "gorra"),
    ("ana", "playera"),
    ("luis", "pantalon"),
    ("marta", "gorra"),
    ("marta", "gorra"),
    ("marta", "pantalon")
]

minimo = 10

def clientes_frecuentes(compras, minimo):
    totales = {}
    frecuentes = []
    for cliente, producto in compras:
        if cliente in totales:
            totales[cliente] += 1
        else:
            totales[cliente] = 1
            
    for cliente, cantidad in totales.items():
        if cantidad >= minimo:
            frecuentes.append(cliente)
        
    return frecuentes

print(clientes_frecuentes(compras, minimo))