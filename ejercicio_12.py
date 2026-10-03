
calificaciones = [
    ("ana", 90),
    ("luis", 70),
    ("ana", 80),
    ("marta", 100),
    ("luis", 60),
    ("luis", 80)
]

def promedio_por_alumno(calificaciones):
    datos = {}
    promedio = {}
    for alumno, nota in calificaciones:
        if alumno in datos:
            datos[alumno][0] += nota
            datos[alumno][1] += 1
        else:
            datos[alumno] = [nota, 1]
    
    suma = 0
    conteo = 0
    for alumno, lista in datos.items():
        suma = lista[0]
        conteo = lista[1]
        promedio[alumno] = suma / conteo
    return promedio



print(promedio_por_alumno(calificaciones))