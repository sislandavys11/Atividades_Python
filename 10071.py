def simpar(x,y):
    soma = 0
    if(x<y):
        for i in range(x+1,y):
            if(i%2==1):
                soma+=i
    else:
        for i in range(y+1,x):
            if(i%2==1):
                soma+=i

x = int(input(""))
y = int(input(""))

print(simpar(soma x,y))
    

