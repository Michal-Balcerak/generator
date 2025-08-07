import random
import sympy
from funkcje import *

'''Działania na ułamkach'''

# dodawanie i odejmowanie - ten sam mianownik
def tworz_dzialanie_1():

    out = ''

    N = 26 #największa liczba całkowita jaka może się wylosować
    M = 15 #największy mianownik jaki może się wylosować

    m = random.randint(2, M) #mianownik

    l_1 = 0 #licznik pierwszej liczby
    while l_1 == 0 or l_1 % m == 0:
        l_1 = random.randint(-(m * N), m*N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    l_2 = 0 #licznik drugiej liczby
    while l_2 == 0 or l_2 % m == 0:
        l_2 = random.randint(-(m * N), m * N)
    ulamek_2 = sympy.sympify(f'{l_2}/{m}')
    tex2 = konwersja_ulamek_liczba_mieszana(ulamek_2)

    w = ''
    if l_2 > 0:
        w = '+'

    out = out + tex1 + w + tex2

    #obliczanie wyniku:
    dzialanie = str(l_1) + '/' + str(m) + '+' + str(l_2) + '/' + str(m)
    wynik = sympy.sympify(dzialanie)
    wynik_tex = konwersja_ulamek_liczba_mieszana(wynik)
    rozwiazanie = wynik_tex

    return (out, rozwiazanie)

# dodawanie i odejmowanie - dowolny mianownik
def tworz_dzialanie_2():

    out = ''

    N = 26 #największa liczba całkowita jaka może się wylosować
    M = 15 #największy mianownik jaki może się wylosować

    m1 = random.randint(2, M) #mianownik
    m2 = random.randint(2, M) #mianownik

    l_1 = 0 #licznik pierwszej liczby
    while l_1 == 0 or l_1 % m1 == 0:
        l_1 = random.randint(-(m1 * N), m1*N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m1}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    l_2 = 0 #licznik drugiej liczby
    while l_2 == 0 or l_2 % m2 == 0:
        l_2 = random.randint(-(m2 * N), m2 * N)
    ulamek_2 = sympy.sympify(f'{l_2}/{m2}')
    tex2 = konwersja_ulamek_liczba_mieszana(ulamek_2)

    w = ''
    if l_2 > 0:
        w = '+'

    out = out + tex1 + w + tex2

    #obliczanie wyniku:
    dzialanie = str(l_1) + '/' + str(m1) + '+' + str(l_2) + '/' + str(m2)
    wynik = sympy.sympify(dzialanie)
    wynik_tex = konwersja_ulamek_liczba_mieszana(wynik)
    rozwiazanie = wynik_tex

    return (out, rozwiazanie)

# mnożenie i dzielenie
def tworz_dzialanie_3():
    out = ''

    x = random.randint(0, 1) # 0 - mnożenie, 1 - dzielenie

    N = 7  # największa liczba całkowita jaka może się wylosować
    M = 5  # największy mianownik jaki może się wylosować

    m1 = random.randint(2, M)  # mianownik1

    l_1 = 0 #licznik pierwszej liczby
    while l_1 == 0 or l_1 % m1 == 0:
        l_1 = random.randint(-(m1 * N), m1 * N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m1}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    m2 = random.randint(2, M)  # mianownik2
    l_2 = 0 #licznik drugiej liczby
    while l_2 == 0 or l_2 % m2 == 0:
        l_2 = random.randint(-(m2 * N), m2 * N)
    ulamek_2 = sympy.sympify(f'{l_2}/{m2}')
    tex2 = konwersja_ulamek_liczba_mieszana(ulamek_2)

    w = ''
    if x == 0:
        w = '\\cdot'
    elif x == 1:
        w = ':'
    e = ''
    f = ''
    if l_2 < 0:
        e = '('
        f = ')'
    out = out + tex1 + w + e + tex2 + f

    # obliczanie wyniku:
    g = ''
    if x == 0:
        g = '*'
    elif x == 1:
        g = '/'

    dzialanie = str(l_1) + '/' + str(m1) + g + '(' + str(l_2) + '/' + str(m2) + ')'
    wynik = sympy.sympify(dzialanie)
    wynik_tex = konwersja_ulamek_liczba_mieszana(wynik)
    rozwiazanie = wynik_tex

    return (out, rozwiazanie)

# dodawanie i odejmowanie - ułamki dziesiętne
def tworz_dzialanie_4():
    out = ""
    a = -20 #dolny zakres
    b = 20 #górny zakres
    d = 2 #ile miejsc po przecinku

    x1 = random.uniform(a, b)
    x1 = round(x1, d)
    if x1.is_integer():
        x1 = int(x1)

    x2 = random.uniform(a, b)
    x2 = round(x2, d)
    if x2.is_integer():
        x2 = int(x2)

    expr = sympy.Rational(str(x1)) + sympy.Rational(str(x2))

    rozwiazanie = str(float_to_polish_string(float(expr.simplify()))) #zmiana na float z przecinkiem
    w = ''
    if x2>=0:
        w = '+'
    out = out + float_to_polish_string(x1) + w + float_to_polish_string(x2)

    return (out, rozwiazanie)

# ułamki dziesiętne - mnożenie
def tworz_dzialanie_5():
    out = ""
    a = -20 #dolny zakres
    b = 20 #górny zakres
    d = 1 #ile miejsc po przecinku

    x1 = random.uniform(a, b)
    x1 = round(x1,d)
    if x1.is_integer():
        x1 = int(x1)

    x2 = random.uniform(a, b)
    x2 = round(x2, d)
    if x2.is_integer():
        x2 = int(x2)

    expr = sympy.Rational(str(x1)) * sympy.Rational(str(x2))

    rozwiazanie = str(float_to_polish_string(float(expr.simplify()))) #zmiana na float z przecinkiem

    out = out + float_to_polish_string(x1) + "\\cdot"
    if x2 < 0:
        out += "("
    out += float_to_polish_string(x2)
    if x2 < 0:
        out += ")"

    return (out, rozwiazanie)





