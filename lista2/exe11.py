def multiplicacao_recursiva(n1, n2):
    if n2 == 0:
        return 0
    elif n2 == 1:
        return n1
    else:
        return n1 + multiplicacao_recursiva(n1, n2 - 1)


numero1 = int(input("escolha um numero :"))
numero2 = int(input("escolha um numero :"))
resultado = multiplicacao_recursiva(numero1, numero2)
print(f'O resultado da multiplicação de {numero1} por {numero2} é {resultado}')
