def subtotal(codigo, quantidade):
    if (codigo == 1):
        return quantidade*4.00
    elif (codigo == 2):
        return quantidade*4.50
    elif (codigo == 3):
        return quantidade*5.00
    elif (codigo == 4):
        return quantidade*2.00
    elif (codigo == 5):
        return quantidade*1.50



linhaLida = input().split()
codigo = int(linhaLida[0])
quantidade = int(linhaLida[1])
print("Total: R$ %.2f" %subtotal(codigo, quantidade))

    
