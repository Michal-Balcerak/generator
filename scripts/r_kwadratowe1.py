import random

def tworz_rownanie_1():
    '''Współczynniki całkowite, pierwiastki całkowite, postać ogólna'''

    a = random.randint(1, 4)
    if random.randint(0, 1) == 0:
        a = a * (-1)

    w = 1
    if random.randint(1, 5) > 1: #2 rozwiązania

        x1 = random.randint(-9, 9)
        x2 = random.randint(-9, 9)


        b = (-1) * (x1 + x2) * a
        c = x1 * x2 * a

    else:  # 0 rozwiązań
        w = 0
        q = 1
        while q:
            b = random.randint(-15, 15)
            c = random.randint(-15, 15)
            if b ** 2 - 4 * a * c < 0:
                q = 0

    if a == 1:
        a = ' '
    elif a == -1:
        a = '-'
    a = str(a)

    if b == 1:
        b = '+'
    elif b == -1:
        b = '-'
    elif b > 0:
        b = '+' + str(b)

    if c > 0:
        c = '+' + str(c)

    out = ''
    out += a
    out += 'x^2'
    if b:
        out += str(b)
        out += 'x'
    if c:
        out += str(c)

    out += '=0'

    if w:
        rozwiazania = [x1, x2]
    else:
        rozwiazania = 0

    return (out, rozwiazania)


