usuarios_registrados = [
    "Carlos",
    "Juan",
    "María",
    "Pedro",
    "Luis"
]

usuarios_activos = [
    "Juan",
    "Pedro",
    "Ana",
    "Carlos"
]

def usuarios_registrados_no_activos(usuarios_registrados, usuarios_activos):
    setR = set(usuarios_registrados)
    setA = set(usuarios_activos)
    
    no_activos = setR.difference(setA)
    
    return no_activos

res = usuarios_registrados_no_activos(usuarios_registrados, usuarios_activos)
print(f"usuarios registrados pero no activos: {res}")