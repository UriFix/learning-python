
ventas = [
    ("Carlos", "playera"),
    ("Juan", "pantalon"),
    ("Carlos", "playera"),
    ("María", "gorra"),
    ("Juan", "playera"),
    ("Carlos", "pantalon"),
    ("María", "playera"),
    ("Juan", "playera")
]

def producto_mas_vendido(ventas):
    contador = {}
    
    for persona, producto in ventas:
        if producto in contador:
            contador[producto] += 1
        else:
            contador[producto] = 1
            
            
    mayor = 0
    producto_mayor = ""
    
    for producto, cantidad in contador.items():
        if cantidad > mayor:
            mayor = cantidad
            producto_mayor = producto
            
    return producto_mayor

respuesta = producto_mas_vendido(ventas)

print(respuesta)