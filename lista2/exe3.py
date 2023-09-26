import math


def inverte(num):
    if num < 10:
        return num

    q = num // 10
    q = inverte(q)

    r = num % 10
    inv = r * 10 ** (math.floor(math.log10(q) + 1)) + q

    return inv


print(inverte(2665351))
