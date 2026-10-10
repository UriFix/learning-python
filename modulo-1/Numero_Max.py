

def numero_mas_frecuente(numeros):

    if not numeros:

        return
    numeros = [1, 2, 3, 4, 5]
    contador = {}

    for numero in numeros:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1

    mayor = 0
    numero_mayor = 0

    for numero in contador:
        if contador[numero] > mayor:
            mayor = contador[numero]
            numero_mayor = numero

    return numero_mayor

resultado = numero_mas_frecuente([])

print(resultado)