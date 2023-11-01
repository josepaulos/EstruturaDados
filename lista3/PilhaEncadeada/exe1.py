#Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.

def maiorElmento(pilha):
    if not pilha:
        return None
    
    maior = pilha.pop()
    while pilha:
        elemento= pilha.pop()
        if elemento > maior:
            maior = elemento
    return maior

pilha = [3,2,1,5,6,3,3,10]

maior_elemento = maiorElmento(pilha)
if maior_elemento is not None:
    print(f"O maior elemento na pilha é: {maior_elemento}")
else:
    print("A pilha está vazia.")