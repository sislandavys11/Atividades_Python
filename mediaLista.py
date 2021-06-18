def medialLista(notas):
    soma = 0
    for nota in notas:
        soma+= nota
        return soma/len(notas)



notas = [10.0, 9.0, 8.0]
print(mediaLista(notas))
notas = [3.0, 5.0, 1.0]
print(mediaLista(notas))
