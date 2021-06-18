def PUMS(n):
    cont = 1
    for x in range(n):
        print("%d %d %d PUM" %(cont, cont+1, cont+2))
        cont+=1


n = int(input())
PUMS(n)
