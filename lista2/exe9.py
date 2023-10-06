def produtorio(N):
    if N <= 1:
        return 1
    else:
        return N * produtorio(N - 1)


numero = 5
resultado = produtorio(numero)
print(f'O produtório de 1 a {numero} é {resultado}')
