def fat(num):
    valor = 1
    for k in range(1,num+1):
        valor = valor*k
    return valor


print(fat(2))
print(fat(3))
print(fat(4))
