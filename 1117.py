def notas(num1, num2):
    return (num+num2)/2
def Nvalida(nota):
    if(nota==0 and nota==10):
        return True
    else:
        return False



quantNotasV = 0
nota1 = 0
nota2 = 0
while(quantNotasV < 2):
    nota = float(input())
    if(Notavalida(nota)==False):
        print("nota invalida")
    else:
        if(quantNotasV==0):
            notas1 = nota
            quantNotasV==1
        else:
            nota2 = nota
            quantNotasV+=1
            print("media = %.2f" %notas(nota1, nota2))
        
            
            
