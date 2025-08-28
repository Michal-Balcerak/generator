import random
from sympy import simplify



def strona_rownania(x):
    value=0
    out =''
    weights = [1 for _ in range(21)]
    weights[10] = 0
    a = random.choices(list(range(-10, 11)), weights=weights)[0]
    b = random.choices(list(range(-10, 11)), weights=weights)[0]
    c = random.choices(list(range(-10, 11)), weights=weights)[0]
    d = random.choices(list(range(-10, 11)), weights=weights)[0]


    if a!=1:
        if a!=-1:
            p1 = str(a)
        else:
            p1 = '-'
    else:
        p1 = ''
    p1 += 'x'

    p2 = ''
    # z lub bez komponentu (cx+d)
    y = random.choices([0, 1], weights=[1, 5])[0]
    if y:
        if b!=1:
            if b!=-1:
                p2+= str(b)
            else:
                p2+= '-'
        p2 += "("
        # (cx+d) lub (d+cx)
        q = random.choices([0, 1], weights=[1, 1])[0]
        if q:
            if c!=1:
                if c!=-1:
                    p2 += str(c)
                else:
                    p2 += '-'
            p2 += 'x'
            if d > 0:
                p2 += "+"
            p2 += str(d)
        else:
            p2 += str(d)
            if c > 0:
                p2 += "+"
            if c != 1:
                if c != -1:
                    p2 += str(c)
                else:
                    p2 += '-'
            p2 += 'x'
        p2 += ")"

    # p1+p2 lub p2+p1
    w = random.choices([0, 1], weights=[1, 1])[0]
    if w:
        out += p1
        if y:
            if b > 0:
                out += "+"
        out += p2
    else:
        out += p2
        if y:
            if a > 0:
                out += "+"
        out += p1

    if y:
        value = simplify(f"{a}*{x} + {b}*({c}*{x}+{d})")
    else:
        value = simplify(f"{a}*{x}")
    #out+= f" @@@ a={a}, b={b}, c={c}, d={d} @@@"
    #out += f"@@@ {value} @@@"
    return (out, value)

# ax+b(cx+d)+z=ex+f(gx+h)
def tworz_rownanie_0():
    out = ''
    x = random.randint(-15,15)


    out1, lewa_value = strona_rownania(x)
    out2, prawa_value = strona_rownania(x)
    z = simplify(prawa_value - lewa_value)

    out += out1
    if z!=0:
        w = random.choices([0, 1], weights=[1, 1])[0]
        if w:
            if z>0:
                out += "+"
            out += str(z)
            out += "="
            out += out2
        else:
            out += "="
            out += out2
            if z < 0:
                out += "+"
            out += str(-z)
    else:
        out += "="
        out += out2

    return (out, [x])
