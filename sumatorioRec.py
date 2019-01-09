def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0

print(sumatorio(4))

def factorial(n)