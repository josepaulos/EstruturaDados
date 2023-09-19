def somaVetor(lista):
    if lista == []:
        return 0

    return lista[0] + somaVetor(lista[1:])


print(somaVetor([1, 1, 1, 1]))
