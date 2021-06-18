def raizQuadrada(num):
    valorRaiz = 1
    while((valorRaiz*valorRaiz) <= num):
        if((valorRaiz*valorRaiz) == num):
            return valorRaiz
        elif((valorRaiz*valorRaiz) > num):
            return valorRaiz-1
        else:
            valorRaiz+=1



print(raizQuadrada(4))
print(raizQuadrada(9))
print(raizQuadrada(16))
