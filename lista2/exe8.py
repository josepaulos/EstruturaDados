def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)


x = int(input("escolha um numero inteiro:"))
y = int(input("escolha um numero interio:"))
resultado = mdc(x, y)
print(f'O MDC de {x} e {y} é {resultado}')
