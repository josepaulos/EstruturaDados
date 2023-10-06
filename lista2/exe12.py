def imprimir_naturais(N, atual=0):
    if atual <= N:
        print(atual)
        imprimir_naturais(N, atual + 1)


numero = int(input("escolha um numero :"))
print(f'Números naturais de 0 a {numero}:')
imprimir_naturais(numero)
