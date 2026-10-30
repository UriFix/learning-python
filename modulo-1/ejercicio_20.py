


def contar_lineas(nombre_archivo):
    try:
        with open(nombre_archivo) as f:
            contador = 0
            for linea in f:
                contador += 1
            return contador
    except FileNotFoundError:
        print(f"no encontre {nombre_archivo}")
        return None

print(contar_lineas("notas.txt"))