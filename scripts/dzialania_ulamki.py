import random
import sympy
from funkcje import *

# słownik z działaniami - do losowania działań
ops = {
    0: "+",  # +
    1: "-",  # -
    2: "*",  # *
    3: "/"  # /
}

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

def tworz_dzialanie_4():
    out = ''

    q = random.randint(2, 3)  # pierwsze dzialanie (mnozenie/dzielenie)
    w = random.randint(0, 1)  # drugie dzialanie (dodawanie/odejmowanie)

    N = 26  # największa liczba całkowita jaka może się wylosować
    M = 15  # największy mianownik jaki może się wylosować

    m1 = random.randint(2, M)  # mianownik
    m2 = random.randint(2, M)  # mianownik
    m3 = random.randint(2, M)  # mianownik

    l_1 = 0  # licznik pierwszej liczby
    while l_1 == 0 or l_1 % m1 == 0:
        l_1 = random.randint(-(m1 * N), m1 * N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m1}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    l_2 = 0  # licznik drugiej liczby
    while l_2 == 0 or l_2 % m2 == 0:
        l_2 = random.randint(-(m2 * N), m2 * N)
    ulamek_2 = sympy.sympify(f'{l_2}/{m2}')
    tex2 = konwersja_ulamek_liczba_mieszana(ulamek_2)

    l_3 = 0  # licznik trzeciej liczby
    while l_3 == 0 or l_3 % m3 == 0:
        l_3 = random.randint(-(m3 * N), m3 * N)
    ulamek_3 = sympy.sympify(f'{l_3}/{m3}')
    tex3 = konwersja_ulamek_liczba_mieszana(ulamek_3)

    # obliczanie wyniku:
    dzialanie = str(l_1) + '/' + str(m1) + ops[q] + "(" + str(l_2) + '/' + str(m2) + ops[w] + str(l_3) + '/' + str(m3) + ")"
    wynik = sympy.sympify(dzialanie)
    wynik_tex = konwersja_ulamek_liczba_mieszana(wynik)
    rozwiazanie = wynik_tex

    out += tex1
    if ops[q]=="*":
        out += "\\cdot"
    elif ops[q]=="/":
        out += ":"
    out += "("
    out += tex2
    out += ops[w]
    if l_3 < 0:
        out += "("
    out += l_3
    if l_3 < 0:
        out += ")"
    out += ")"

    return (out, rozwiazanie)


# dodawanie i odejmowanie - ułamki dziesiętne
def tworz_dzialanie_5():
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
    obliczone = f"{float(expr.simplify()):g}"
    rozwiazanie = float_to_polish_string(obliczone)

    w = ''
    if x2>=0:
        w = '+'
    out = out + float_to_polish_string(x1) + w + float_to_polish_string(x2)

    return (out, rozwiazanie)

# ułamki dziesiętne - mnożenie
def tworz_dzialanie_6():
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
    obliczone = f"{float(expr.simplify()):g}"
    rozwiazanie = float_to_polish_string(obliczone)

    out = out + float_to_polish_string(x1) + "\\cdot"
    if x2 < 0:
        out += "("
    out += float_to_polish_string(x2)
    if x2 < 0:
        out += ")"

    return (out, rozwiazanie)

# a@b@c
# a,b,c - ulamki dziesietne
# @ - działanie
def tworz_dzialanie_7():
    out = ""
    a = -20  # dolny zakres
    b = 20  # górny zakres
    d = 1  # ile miejsc po przecinku

    x1 = random.uniform(a, b)
    x1 = round(x1, d)
    if x1.is_integer():
        x1 = int(x1)

    x2 = random.uniform(a, b)
    x2 = round(x2, d)
    if x2.is_integer():
        x2 = int(x2)

    x3 = random.uniform(a, b)
    x3 = round(x3, d)
    if x3.is_integer():
        x3 = int(x3)

    # na razie bez dzielenia
    q = random.randint(0,2) #pierwsze dzialanie (dodawanie/odejmowanie/mnozenie/dzielenie)
    w = random.randint(0,2) #drugie dzialanie (dodawanie/odejmowanie/mnozenie/dzielenie)


    s = f"{x1} {ops[q]} {x2} {ops[w]} {x3}"
    expr = sympy.parsing.sympy_parser.parse_expr(s)
    obliczone = f"{float(expr.simplify()):g}"
    rozwiazanie = float_to_polish_string(obliczone)

    out += float_to_polish_string(x1)
    if ops[q]=="*":
        out+="\\cdot"
    elif ops[q]=="/":
        out+=":"
    else:
        out+= ops[q]
    if x2 < 0:
        out += "("
    out += float_to_polish_string(x2)
    if x2 < 0:
        out += ")"
    if ops[w] == "*":
        out += "\\cdot"
    elif ops[w] == "/":
        out += ":"
    else:
        out += ops[w]
    if x3 < 0:
        out += "("
    out += float_to_polish_string(x3)
    if x3 < 0:
        out += ")"


    return (out, rozwiazanie)

# a @ (b & c)
# a,b,c - ulamki dziesietne
# @ - mnozenie lub dzielenie
# & - dodawanie lub odejmowanie
def tworz_dzialanie_8():
    out = ""
    a = -20  # dolny zakres
    b = 20  # górny zakres
    d = 1  # ile miejsc po przecinku

    x1 = random.uniform(a, b)
    x1 = round(x1, d)
    if x1.is_integer():
        x1 = int(x1)

    x2 = random.uniform(a, b)
    x2 = round(x2, d)
    if x2.is_integer():
        x2 = int(x2)

    x3 = random.uniform(a, b)
    x3 = round(x3, d)
    if x3.is_integer():
        x3 = int(x3)

    #q = random.randint(2, 3)  # pierwsze dzialanie (mnozenie/dzielenie)
    q =2 #na razie bez dzielenia
    w = random.randint(0, 1)  # drugie dzialanie (dodawanie/odejmowanie)

    s = f"{x1} {ops[q]} ({x2} {ops[w]} {x3})"
    expr = sympy.parsing.sympy_parser.parse_expr(s)
    obliczone = f"{float(expr.simplify()):g}"
    rozwiazanie = float_to_polish_string(obliczone)

    out += float_to_polish_string(x1)
    if ops[q]=="*":
        out += "\\cdot"
    elif ops[q]=="/":
        out += ":"
    out += "("
    out += float_to_polish_string(x2)
    out += ops[w]
    if x3 < 0:
        out += "("
    out += float_to_polish_string(x3)
    if x3 < 0:
        out += ")"
    out += ")"

    return (out, rozwiazanie)




