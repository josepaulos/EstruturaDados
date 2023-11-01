def imprimir_pares_decrescente(N):
    if N < 0:
        return
    if N % 2 == 0:
        print(N)
    imprimir_pares_decrescente(N - 2)


numero = int(input("escolha um numero :"))
print(f'Números pares de {numero} a 0 (ordem decrescente):')
imprimir_pares_decrescente(numero)
