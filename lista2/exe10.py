def contar_digitos(N, K):
    if N < 10:
        return 1 if N == K else 0
    else:
        ultimo_digito = N % 10
        ocorrencias = 1 if ultimo_digito == K else 0
        return ocorrencias + contar_digitos(N // 10, K)


numero = int(input("digite uma sequecia com 10 numeros aleatorios:"))
digito = int(input("escolha um numero para ver quantas vezes se repete:"))
ocorrencias = contar_digitos(numero, digito)
print(f'O dígito {digito} ocorre {ocorrencias} vezes em {numero}')
