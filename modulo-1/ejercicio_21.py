

def frecuencia_lineas(nombre_archivo):

    try:
        with open(nombre_archivo) as f:
            contador = {}
            for compra in f:
                compra = compra.strip()
                if compra in contador:
                    contador[compra] += 1
                else:
                    contador[compra] = 1
            return contador
    except FileNotFoundError:
        print(f"no encontre archivo: {nombre_archivo}")
        return None



print(frecuencia_lineas("archivos-txt/compras.txt"))
