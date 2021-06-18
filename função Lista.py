def leListaNomes(n):
    nomes = []
    for s in range(n):
        nome = str.upper(input("Digite um nome: \n"))
        nomes.append(nome)
    return nomes

def existeNomeEmLista(nome, lista):
    for k in lista:
        if (nome == k):
            return True
        return False


                 


x = int(input("Quantos nomes? \n"))
lista = leListaNomes(x)
print(lista)
lista.sort()
print("Lista Ordenada",lista)
nomePesquisado = input("Qual o nome a pesquisar? \n")
if(existeNomeEmLista(nomePesquisado, lista)
                 

















