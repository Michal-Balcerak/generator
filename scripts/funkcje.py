from fractions import Fraction

def NWD(a, b):
    while a!=b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a

def konwersja_ulamek_liczba_mieszana(ulamek):
    out = ''

    num = Fraction(str(ulamek))
    n, d = (num.numerator, num.denominator)

    minus = False
    if n < 0:
        minus = True
        n = -n

    c = n // d  # calosci
    r = n - c * d
    if minus:
        out += '-'

    if c != 0 or r == 0:
        out = out + str(c)
    if r != 0:
        out = out + '\\frac{' + str(r) + '}{' + str(d) + '}'

    return out

def float_to_polish_string(f):
    return str(f).replace('.', ',')