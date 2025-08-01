import random
from sympy import symbols, expand, latex, solve

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

def tworz_rownanie_3b():
    '''Grupowanie wyrazów - Współczynniki całkowite'''
    out = ""
    rozwiazania = []

    while True:
        a, b, c = 0, 0, 0
        r = random.randint(1,3)
        choice = list(range(-9, 10))
        choice.remove(0)
        if r == 1:
            # ax^2 + bx
            a = random.choice(choice)
            b = random.choice(choice)

        elif r == 2:
            #ax^2+c
            a = random.choice(choice)
            c = random.choice(choice)

        else:
            #bx+c
            b = random.choice(choice)
            c = random.choice(choice)

        d,e,f,g,h,i = 0,0,0,0,0,0

        p = random.randint(1, 3) #ax^2 lub bx lub c
        q = random.randint(1, 3) #ax^2 lub bx lub c

        choice2 = list(range(-8, 9))
        choice2.remove(0)

        if p == 1:
            d = random.choice(choice2)
        elif p == 2:
            e = random.choice(choice2)
        else:
            f = random.choice(choice2)

        if q == 1:
            g = random.choice(choice2)
        elif q == 2:
            h = random.choice(choice2)
        else:
            i = random.choice(choice2)

        '''Współczynniki:
        przy x^4: (ad+ag)
        przy x^3: (bd+ae+bg+ah)
        przy x^2: (cd+be+af+cg+bh+ai)
        przy x: (ce+bf+ch+bi)
        wolny: (cf+ci)'''

        #Tylko z niezerowymi współczynnikami:

        if b*d+a*e+b*g+a*h == 0:
            continue
        elif c*d+b*e+a*f+c*g+b*h+a*i == 0:
            continue
        elif c*e+b*f+c*h+b*i == 0:
            continue
        elif c*f+c*i == 0:
            continue
        else:
            break

    x = symbols('x')

    expr = (d * x ** 2 + e * x + f) * (a * x ** 2 + b * x + c) + (g * x ** 2 + h * x + i) * (a * x ** 2 + b * x + c)

    expanded_expr = expand(expr)
    latex_form = latex(expanded_expr)

    solutions = solve(expr, x)
    real_solutions = [sol for sol in solutions if sol.is_real]

    latex_real_solutions = [latex(sol) for sol in real_solutions]

    out += str(latex_form)
    out += "=0"
    rozwiazania = latex_real_solutions

    return (out, rozwiazania)