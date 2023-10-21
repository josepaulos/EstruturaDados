#1. Implemente a função remove utilizando a função busca. 

def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def remove(lista, elemento):
    indice = busca(lista,elemento)
    if indice != -1:
        del lista[indice]
        return True
    else:
        return False
    

lista1=[1,2,3,4,5,6,7,8,9]

elemento  =3
elemento  =5


if remove(lista1,elemento):
    print(f'O elemento {elemento} foi removido da lista.')
else:
    print(F'O elemento {elemento} não foi encontrado')


print(lista1)