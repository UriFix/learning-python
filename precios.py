precios = {
    "pan": 25,
    "leche": 30,
    "huevos": 40
}

for articulo, precio in precios.items():
    print(f"El {articulo} cuesta {precio}")


frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]

contador = {}

for fruta in frutas:
    if fruta in contador:
        contador[fruta] += 1
    else:
        contador[fruta] = 1

mayor = 0
fruta_mayor = 0

for fruta in contador:
    if contador[fruta] > mayor:
        mayor = contador[fruta]
        fruta_mayor = fruta


print(fruta_mayor)
