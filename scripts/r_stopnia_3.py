import random

def tworz_rownanie_3():
    '''Współczynniki całkowite, pierwiastki całkowite, postać ogólna'''
    x1 = random.randint(-15, 15)

    a = random.randint(1, 4)
    if random.randint(0, 1) == 0:
        a = a * (-1)

    w = 1
    if random.randint(1, 5) > 1:
        x2 = random.randint(-15, 15)
        x3 = random.randint(-15, 15)
        b = (-1) * (x1 + x2 + x3) * a
        c = (x1*x2 + x1*x3 + x2*x3) * a
        d = (-1) * x1 * x2 * x3 * a

    else:
        w = 0
        e = 1
        while e:
            p = random.randint(-3, 3)
            q = random.randint(-6, 6)
            r = random.randint(-6, 6)
            if q**2-4*p*r < 0:
                e = 0

        b = (q-p*x1)*a
        c = (r-x1*q)*a
        d = (-x1*r)*a
        a = a * p


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

    if c == 1:
        c = '+'
    elif c == -1:
        c = '-'
    elif c > 0:
        c = '+' + str(c)

    if d == 1:
        d = '+'
    elif d == -1:
        d = '-'
    elif d > 0:
        d = '+' + str(d)

    out = ''
    out += a
    out += 'x^3'
    if b:
        out += str(b)
        out += 'x^2'
    if c:
        out += str(c)
        out += 'x'
    if d:
        out += str(d)
    out += '=0'

    if w:
        rozwiazania = [x1, x2, x3]
    else:
        rozwiazania = [x1]


    return (out, rozwiazania)