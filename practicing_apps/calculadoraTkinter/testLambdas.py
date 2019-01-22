def sumaTodos(limitTo):
    resultado = 0
    for n in range(0, limitTo+1):
        resultado += n
    return resultado

def sumaTodosCuadrado(limitTo):
    resultado = 0
    for n in range(0, limitTo+1):
        resultado += n ** 2
    return resultado


def sumaTodosF(limitTo, f):
    resultado = 0
    for n in range(0, limitTo+1):
        resultado += f(n)
    return resultado


