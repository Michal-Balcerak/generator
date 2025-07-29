import random

'''Współczynniki całkowite, pierwiastki całkowite, postać niezredukowana'''

def strona_rownania():
    out = ''
    # nawias typu ax(bx+c)
    if random.randint(0, 1):
        a1 = random.randint(1, 12)
        if random.randint(0, 1):
            a1 *= -1
        if a1==-1:
            out+='-'
        elif a1!=1:
            out += str(a1)
        out += 'x'
        out += '('

        b1 = random.randint(1, 12)
        if random.randint(0, 1):
            b1 *= -1
        if b1 == -1:
            out += '-'
        elif b1 != 1:
            out += str(b1)
        out += 'x'

        c1 = random.randint(1, 12)
        if random.randint(0, 1):
            c1 *= -1
        if c1 > 0:
            out += '+'
        out += str(c1)
        out += ')'
    else:
        a1 = 0
        b1 = 0
        c1 = 0

    # ax^2
    if random.randint(0, 1):
        a2 = random.randint(1, 12)
        if random.randint(0, 1):
            a2 *= -1
        if out and a2 > 0:
            out += '+'
        if a2==-1:
            out+='-'
        elif a2!=1:
            out += str(a2)
        out += 'x^2'
    else:
        a2 = 0

    # bx
    if random.randint(0, 1):
        b2 = random.randint(1, 12)
        if random.randint(0, 1):
            b2 *= -1
        if out and b2 > 0:
            out += '+'
        if b2 == -1:
            out += '-'
        elif b2 != 1:
            out += str(b2)
        out += 'x'
    else:
        b2 = 0

    # c
    if random.randint(0, 1):
        c2 = random.randint(1, 12)
        if random.randint(0, 1):
            c2 *= -1
        if out and c2 > 0:
            out += '+'
        out += str(c2)
    else:
        c2 = 0

    # # nawias typu a(bx+c)
    # if random.randint(0, 1):
    #     a3 = random.randint(2, 12)
    #     if random.randint(0, 1):
    #         a3 *= -1
    #     if out and a3 > 0:
    #         out += '+'
    #     out += str(a3)
    #     out += '('
    #
    #     b3 = random.randint(1, 12)
    #     if random.randint(0, 1):
    #         b3 *= -1
    #
    #     if b3 == -1:
    #         out += '-'
    #     elif b3 != 1:
    #         out += str(b3)
    #     out += 'x'
    #
    #     c3 = random.randint(1, 12)
    #     if random.randint(0, 1):
    #         c3 *= -1
    #     if c3 > 0:
    #         out += '+'
    #     out += str(c3)
    #     out += ')'
    # else:
    #     a3 = 0
    #     b3 = 0
    #     c3 = 0
    a3 = b3 = c3 = 0

    a = a1*b1+a2
    b = a1*c1+b2+a3*b3
    c = c2+a3*c3
    wynik = (out, a, b, c)

    return wynik


def tworz_rownanie_2():

    a = random.randint(1, 4)
    if random.randint(0, 1) == 0:
        a = a * (-1)

    w = 1
    if random.randint(1, 5) > 1:
        x1 = random.randint(-15, 15)
        x2 = random.randint(-15, 15)
        b = (-1) * (x1 + x2) * a
        c = x1 * x2 * a

    else: #0 rozwiązań
        w = 0
        q = 1
        while q:
            b = random.randint(-9, 9)
            c = random.randint(-9, 9)
            if b ** 2 - 4 * a * c < 0:
                q = 0

    output = ''

    lewa = strona_rownania()
    prawa = strona_rownania()


    if lewa[0] == '':
        output += '0'
    else:
        output += lewa[0]
    output += '='

    output += prawa[0]

    x = a-lewa[1]+prawa[1]
    y = b-lewa[2]+prawa[2]
    z = c-lewa[3]+prawa[3]


    dopis_z_prawej=0

    if x:
        x=(-1)*x
        if prawa[0] and x>0:
            output+='+'
        if x == -1:
            output += '-'
        elif x != 1:
            output += str(x)

        output+='x^2'
        dopis_z_prawej =1

    if y:
        y=(-1)*y
        if ((prawa[0]or dopis_z_prawej) and y > 0):
            output += '+'
        if y == -1:
            output += '-'
        elif y != 1:
            output += str(y)

        output += 'x'
        dopis_z_prawej =1

    if z:
        z = (-1)*z
        if (prawa[0]or dopis_z_prawej) and z > 0:
            output += '+'
        output += str(z)

    if w:
        rozwiazania = [x1, x2]
    else:
        rozwiazania = []

    return (output, rozwiazania)




