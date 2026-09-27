usuarios_a = [
    "Carlos",
    "Juan",
    "María",
    "Pedro"
]

usuarios_b = [
    "Juan",
    "Pedro",
    "Luis",
    "Ana"
]



def usuarios_en_ambas(usuarios_a, usuarios_b):
    setusuarios_a = set(usuarios_a)
    setusuarios_b = set(usuarios_b)
    
    unicos = setusuarios_a.intersection(setusuarios_b)
    
    return unicos

res = usuarios_en_ambas(usuarios_a, usuarios_b)


def usuarios_en_ambas_for(usuarios_a, usuarios_b):
    set_a = set()
    set_b = set()
    
    for usuario in usuarios_a:
        set_a.add(usuario)

    for usuario in usuarios_b:
        set_b.add(usuario)   
        
    unicos_ambas = set_a.intersection(set_b)
    
    return unicos_ambas

res_for = usuarios_en_ambas_for(usuarios_a, usuarios_b)

def usuarios_solo_a(usuarios_a, usuarios_b):
    set_a = set(usuarios_a)
    set_b = set(usuarios_b)

    solo_a = set_a.difference(set_b)
    return  solo_a

res_solo_a = usuarios_solo_a(usuarios_a, usuarios_b)
print(res) 
print(res_for)
print(res_solo_a)