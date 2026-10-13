def f1(lista):
    total = 0
    for x in lista:
        total += x
    return total

def f2(lista):
    for x in lista:
        for y in lista:
            print(x, y)

def f3(lista):
    vistos = set()
    for x in lista:
        if x in vistos:
            return True
        vistos.add(x)
    return False

def f4(lista):
    vistos = []
    for x in lista:
        if x in vistos:
            return True
        vistos.append(x)
    return False

# ===== NOTAS: TIEMPO Y ESPACIO (f1 a f4), n = tamaño de lista =====
#
# f1: un solo for, suma a un número
#     tiempo O(n)   espacio O(1)   (total es una sola variable)
#
# f2: un for DENTRO de otro
#     tiempo O(n^2) espacio O(1)   (no crea ninguna estructura)
#
# f3: for + set (x in set es O(1))
#     tiempo O(n)   espacio O(n)   (peor caso: guarda los n elementos)
#
# f4: for + lista (x in lista es O(n), recorrido escondido)
#     tiempo O(n^2) espacio O(n)
#
# REGLAS:
# - for uno DESPUÉS de otro: se SUMAN
# - for uno DENTRO de otro: se MULTIPLICAN
# - un "in" sobre una LISTA cuenta como un for escondido
# - "in" sobre un set o un diccionario: O(1)
# - espacio = lo que CREO nuevo (la entrada no cuenta)
# - peor caso = el que más trabajo da (aquí, lista sin repetidos)
#
# f3 y f4 hacen lo mismo, pero f4 es más lenta: un solo "in" cuesta
# O(1) en un set y O(n) en una lista, y se ejecuta n veces.