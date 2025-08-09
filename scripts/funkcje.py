from fractions import Fraction
import sympy as sp

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

def float_to_polish_string(expr, prec=20):
    """Zwraca łańcuch z przecinkiem dziesiętnym, bez śmieci z binarnego float."""
    # policz w SymPy z daną precyzją (bez przechodzenia przez float)
    val = sp.N(sp.simplify(expr), prec)   # == expr.evalf(prec)
    # jeśli całkowite, oddaj jako int
    if val.is_integer():
        return str(int(val))
    # w innym wypadku usuń zbędne zera i kropkę na końcu
    s = str(val)
    if "e" in s or "E" in s:
        # jeśli wyszła notacja naukowa, zwiększ precyzję i spróbuj jeszcze raz
        val = sp.N(val, prec + 10)
        s = str(val)
    s = s.rstrip("0").rstrip(".")
    return s.replace(".", ",")