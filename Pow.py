def potencia(num,pot):
    valor = 1
    for k in range(pot):
        valor = valor*num
    return valor

print(potencia(2,2))
print(potencia(2,3))
print(potencia(2,4))
