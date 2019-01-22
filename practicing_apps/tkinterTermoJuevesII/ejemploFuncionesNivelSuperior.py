def suma(limitTo):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += i
    
    return sumatorio

def sumaCuadrado(limitTo):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += i*i
    return sumatorio

def sumaf(limitTo, f):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += f(i)
        
    return sumatorio

def cuadrado(x):
    return x*x

def cuadradoE(x, y):
    return x*x

print(sumaf(4, cuadradoE))