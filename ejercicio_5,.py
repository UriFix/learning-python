
usuarios = [
    "Carlos",
    "Juan",
    "Carlos",
    "María",
    "Juan",
    "Pedro",
    "María",
    "Carlos"
]

def usuarios_unicos(usuarios):
    unicos = set()
    
    for usuario in usuarios:
        unicos.add(usuario)
        
    return unicos

res = usuarios_unicos(usuarios)
    
print(res)