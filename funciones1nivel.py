def normal(i):
    return i

def cuadrado(x):
    return x * x


def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
        
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))