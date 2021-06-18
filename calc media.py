import random


def media(listanumero):
    soma = 0
    for s in (listanumero):
        soma+=s
    return soma/len(listanumero)


def maior(listainteiros):
    m = listainteiros[0]
    for s in (listainteiros):
        if(s > m):
            m = s
    return m



def somadequadrados(listainteiros):
    soma = 0
    for s in listainteiros:
        m = s ** 2
        soma+=m
    return soma


def qimpar(listainteiros):
    cont = 0
    for s in listainteiros:
        if(s%2 == 1):
            cont+=1
    return cont

def spar(listainteiros):
    soma = 0
    for s in listainteiros:
        if(s%2 == 0):
            soma+=s
    return soma

def negativo(listainteiros):
    soma = 0
    for s in listainteiros:
        if(s < 0):
            soma+=s
    return soma


def nump(listapalavras):
    t = len(listapalavras)
    return t
        
        



lista = []
for d in range(100):
    numero = random.randrange(0,1001)
    lista.append(numero)
print(lista)
print("A media eh:",media(lista))
