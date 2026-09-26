ventas = [
    ("Carlos", 500),
    ("Juan", 300),
    ("Carlos", 200),
    ("María", 700),
    ("Juan", 100)
]

def total_ventas(ventas):

    contador = {}

    for persona, cantidad in ventas:
        if (persona) in contador:
            contador[persona] += cantidad
        else:
            contador[persona] = cantidad

    return contador

res = total_ventas(ventas)

def vendedor_mayor(ventas):
    
    contador = {}
    
    for persona, cantidad in ventas:
        if (persona) in contador:
            contador[persona] += cantidad
        else:
            contador[persona] = cantidad
    
    
    mayor = 0
    vendedor_mayor = ""
    
    for persona, cantidad in contador.items():
        if cantidad > mayor:
            mayor = cantidad
            vendedor_mayor = persona
    
    return vendedor_mayor

res1 = vendedor_mayor(ventas)

print(res)
print(res1)


