

def primer_unico(lista):

    conteo = {}

    for x in lista:
        if x in conteo:
            conteo[x] += 1
        else:
            conteo[x] = 1

    for y in lista:
        if conteo[y] == 1:
            return y
    return None



print(primer_unico([4, 5, 4, 5, 5, 7]))
print(primer_unico([1, 1, 2, 2]))