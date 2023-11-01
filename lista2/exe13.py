def imprimir_naturais_decrescente(N):
    if N >= 0:
        print(N)
        imprimir_naturais_decrescente(N - 1)


numero = int(input("escolha um numero :"))  
print(f'Números naturais de {numero} a 0 (ordem decrescente):')
imprimir_naturais_decrescente(numero)
