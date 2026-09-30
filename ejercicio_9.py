movimientos = [("gorra", "entrada", 3), ("gorra", "salida", 5)]


def stock_actual(movimientos):
    contador = {}

    for producto, movimiento, cantidad in movimientos:
        if movimiento == "entrada" or movimiento == "devolucion":
            if producto in contador:
                contador[producto] += cantidad
            else:
                contador[producto] = cantidad
        elif movimiento == "salida":
            if producto not in contador:
                print(f"no hay stock de {producto}")
            elif contador[producto] < cantidad:
                print(f"stock insuficiente de: {producto} hay: {contador[producto]}, se piden: {cantidad}")
            else:
                contador[producto] -= cantidad
        else: 
            print(f"no existe tal movimiento: {movimiento}")
    return contador

res = stock_actual(movimientos)

print(res)