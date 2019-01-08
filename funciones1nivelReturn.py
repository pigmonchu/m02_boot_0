
def maxi(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    
    return m

def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
        
    return suma / len(l)

funciones = {
    'max': maxi,
    'min': mini,
    'med': media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None



