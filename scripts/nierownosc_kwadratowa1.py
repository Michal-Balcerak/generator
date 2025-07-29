import random

def tworz_nierownosc_1():
    '''Współczynniki całkowite, pierwiastki całkowite, postać ogólna'''
    Q = 0


    a = random.randint(1, 4)
    if random.randint(0, 1) == 0:
        a = a * (-1)

    w = 1
    if random.randint(1, 5) > 1: #2 rozwiązania

        x1 = random.randint(-9, 9)
        x2 = random.randint(-9, 9)


        b = (-1) * (x1 + x2) * a
        c = x1 * x2 * a

        if x1 == x2:
            Q = 1
        else:
            Q = 2

    else:  # 0 rozwiązań
        w = 0
        q = 1
        while q:
            b = random.randint(-15, 15)
            c = random.randint(-15, 15)
            if b ** 2 - 4 * a * c < 0:
                q = 0
                Q = 0

    s=a
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

    x = random.randint(1, 4)
    if x == 1:
        out += '>'
    elif x == 2:
        out += '\geq'
    elif x == 3:
        out += '<'
    elif x == 4:
        out += '\leq'

    out += '0'

    # z - rozwiązanie
    z = 'x\in'
    # Q - liczba rozwiazan
    if Q==2:
        s = max(x1, x2)
        r = min(x1, x2)
    if s>0: #wsp przy x^2>0
        if x ==1: #>
            if Q==0:
                z += '\mathbb{R}'
            elif Q == 1:
                z += "\mathbb{R}'\'backslash\{"
                z += str(x1)
                z += '\}'
            else:
                z += f'(-\infty,{r})\cup({s},+\infty)'

        elif x == 2: #>=
            if Q==0 or Q ==1:
                z += '\mathbb{R}'
            else:
                z += f'(-\infty,{r}\\rangle\cup\langle{s},+\infty)'

        elif x == 3: #<
            if Q==0 or Q==1:
                z += '\emptyset'
            else: #<=
                z += f'({r}, {s})'
        else:
            if Q==0:
                z += '\emptyset'

            elif Q == 1:
                z += '\{'
                z += str(x1)
                z += '\}'
            else:
                z += f'(-\infty,{r}\\rangle\cup\langle{s},+\infty)'
    else: #wsp przy x^2<0
        if x == 1:
            if Q == 0 or Q == 1:
                z += '\emptyset'
            else:
                z += f'({r},{s})'

        elif x == 2:
            if Q == 0:
                z += '\emptyset'
            elif Q == 1:
                z += '\{'
                z += str(x1)
                z += '\}'
            else:
                z += f'\langle{r},{s}'
                z += '\\rangle' ######

        elif x == 3:
            if Q == 0:
                z += '\mathbb{R}'
            elif Q == 1:
                z += '\mathbb{R}'
                z += '\\backslash\{'
                z += str(x1)
                z += '\}'
            else:

                z += f'(-\infty,{r})\cup({s},+\infty)'
        else:
            if Q == 0 or Q ==1:
                z += '\mathbb{R}'
            else:
                z += f'(-\infty,{r}\\rangle\cup\langle{s},+\infty)'




    return (out, 'nierownosc', z)


