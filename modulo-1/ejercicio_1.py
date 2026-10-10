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


     
for producto in count:
    print(producto, count[producto], " unidades")