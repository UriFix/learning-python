productos = ["playera", "pantalon", "playera", "gorra", "pantalon", "playera"]

def contar_productos(productos):
    contador = {}

    for producto in productos:
        if producto in contador:
            contador[producto] += 1
        else:
            contador[producto] = 1



    return contador


resultado = contar_productos(productos)
print(resultado)
