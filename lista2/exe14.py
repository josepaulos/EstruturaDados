def imprimir_pares_crescente(N, atual=0):
    if atual <= N:
        if atual % 2 == 0:
            print(atual)
        imprimir_pares_crescente(N, atual + 1)


numero = int(input("escolha um numero :"))
print(f'Números pares de 0 a {numero} (ordem crescente):')
imprimir_pares_crescente(numero)
