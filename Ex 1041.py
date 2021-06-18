def coordenadas(x,y):
    if(x==0 and y==0):
        return "Origem"
    elif(x>0 and y>0):
        return "Q1"
    elif(x<0 and y>0):
        return "Q2"
    elif(x<0 and y<0):
        return "Q3"
    elif(x>0 and y<0):
        return "Q4"
    elif(x==0):
        return "Eixo Y"
    else:
        return "Eixo X"




linha = input().split()
x = float(linha[0])
y = float(linha[1])
print(coordenadas(x,y))
