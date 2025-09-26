import random
from sympy import expand,symbols, latex

litery = ['a','b','x','y','z','c','d','k','l','m','n','p','q']


#typu (4a+7b)^2 lub (4a+7b)^3
def tworz_wzor1(degree = 2):
    x = random.randint(0,len(litery)-1)
    y = x
    while y == x:
        y = random.randint(0,len(litery)-1)
    a = litery[x]
    b = litery[y]

    c = 0
    while c == 0:
        c = random.randint(-9,9) if degree==2 else random.randint(-6,6)
    d = 0
    while d == 0:
        d = random.randint(-9,9) if degree==2 else random.randint(-6,6)

    a_,b_ = symbols([a,b])
    expr = (c*a_+d*b_)**degree

    c = str(c)
    d = str(d)

    if c == '1':
        c = ""
    elif c == '-1':
        c = "-"

    if d == '1':
        d = "+"
    elif d == '-1':
        d = "-"
    elif int(d) > 0:
        d = "+"+d

    to_show = "(" + c + a + d + b + ")^" + str(degree)


    sol = latex(expand(expr))

    return (to_show, sol)

# typu (3a-9b)(3a+9b)
def tworz_wzor2():
    x = random.randint(0,len(litery)-1)
    y = x
    while y == x:
        y = random.randint(0,len(litery)-1)
    a = litery[x]
    b = litery[y]

    c = random.randint(1,13)
    d = random.randint(1,13)

    a_,b_ = symbols([a,b])
    z = random.randint(0,1)
    expr = (c*a_-d*b_)*(c*a_+d*b_) if z else (c*a_+d*b_)*(c*a_-d*b_)


    c = str(c)
    d = str(d)

    j = random.randint(0,2) #j==0 inversed (a+b) <-> (b+a)

    if j:
        if c == '1':
            c = ""

        if d == '1':
            d = "+"
    else:
        if c == '1':
            c = "+"

        if d == '1':
            d = ""

    p = "(" + c + a + "-" + d + b +")"
    q = "(" + c + a + "+" + d + b + ")" if random.randint(0,2) else "(" + d + b + "+" + c + a + ")"
    to_show = p + q if z else q + p


    sol = latex(expand(expr))

    return (to_show, sol)

def tworz_wzor4(degree=2):
    x = random.randint(0, len(litery) - 1)
    y = x
    while y == x:
        y = random.randint(0, len(litery) - 1)
    a = litery[x]
    b = litery[y]

    c = 0
    while c == 0:
        c = random.randint(-9, 9) if degree == 2 else random.randint(-6, 6)
    d = 0
    while d == 0:
        d = random.randint(-9, 9) if degree == 2 else random.randint(-6, 6)

    exp1 = random.randint(2, 6)
    exp2 = random.randint(2, 6)

    a_, b_ = symbols([a, b])
    expr = (c * a_ ** exp1 + d * b_ ** exp2) ** degree

    c = str(c)
    d = str(d)

    if c == '1':
        c = ""
    elif c == '-1':
        c = "-"

    if d == '1':
        d = "+"
    elif d == '-1':
        d = "-"
    elif int(d) > 0:
        d = "+" + d

    to_show = "(" + c + a + "^" + str(exp1) + d + b + "^" + str(exp2) + ")^" + str(degree)

    sol = latex(expand(expr))

    return (to_show, sol)