productos = [
    "playera",
    "pantalon",
    "playera",
    "gorra",
    "pantalon",
    "playera"
]

count = {}

for producto in productos:
    if producto in count:
        count[producto] += 1
    else:
        count[producto] = 1

mayor = 0

for producto in count:
    if count[producto] > mayor:
        mayor = count[producto]
        prod_mayor = producto
        
print(f"el producto mas vendido fue: {prod_mayor}")
print(f"cantidad: {mayor}")