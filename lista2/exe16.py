def fatorial_duplo(N):
    if N == 1:
        return 1
    else:
        return N * fatorial_duplo(N - 2)


numero = int(input("escolha um numero impa:"))
resultado = fatorial_duplo(numero)
print(f'O fatorial duplo de {numero} é {resultado}')
