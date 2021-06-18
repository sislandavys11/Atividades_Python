def lerdesafios(n):
    lista = []
    for s in range(n):
        desafio = str.upper(input("Digite uma palavra para ser adivinhada"))
        lista.append(desafio)
    return lista


def sorteiaDesafio(desafios):
    tlista = len(desafios)
    posicaosorteada = random.randrange(0, tlista)
    return desafios(posicaosorteada)





def criaDesafioEscondido(palavra):
    lista = []
    tpalavra = len(palavra)
    for s in range(tpalavra):
        lista.append("_")
    return lista


def substituiLetrasNaPalavra(letra, listaMostrada, palavra):
    tpalavra = len(palavra)
    for s in range(tpalavra):
        if(palavra[s] == letra):
            listaMostrada[k] = letra
    
            
    

    
