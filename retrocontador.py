def retrocontador(e):
    print("{},".format(e), end="")
    
    if e > 0:
        retrocontador(e-1)
    

retrocontador(10)

def sumatorio(n):
    
    return n + sumatorio(n-1)