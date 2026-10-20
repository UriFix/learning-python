

def primer_repetido(lista):
    vistos = set()

    for x in lista:
        if x in vistos:
            return x
        vistos.add(x)

    return

print(primer_repetido([3, 7, 2, 7, 3]))
print(primer_repetido([1, 2, 3]))


