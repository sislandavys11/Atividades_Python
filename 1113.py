def coud(x, y):
    if(x < y):
        return"Crescente"
    elif(x > y):
        return "Decrescente"
    else:
        return "Iguais"
    
        
    
        


continuar = True
while continuar:
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    if x == y:
        continuar = False
print(coud(x,y))
