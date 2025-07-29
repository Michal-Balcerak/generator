import random
import sympy
from funkcje import *

'''Działania na ułamkach'''

# dodawanie i odejmowanie - ten sam mianownik
def tworz_dzialanie_1():

    out = ''
    rozwiazanie = ''

    y_1 = random.randint(0, 1) #znak pierwszej liczby
    y_2 = random.randint(0, 1) #znak drugiej liczby

    N = 26 #największa liczba całkowita jaka może się wylosować
    M = 15 #największy mianownik jaki może się wylosować
    LICZBY = []
    for i in range(N):
        LICZBY.append(i+1)


    m = random.randint(2, M) #mianownik

    l_1 = 0
    while l_1 == 0 or l_1 % m == 0:
        l_1 = random.randint(-(m * M), m*N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    l_2 = 0
    while l_2 == 0 or l_2 % m == 0:
        l_2 = random.randint(-(m * M), m * N)
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
    rozwiazanie = ''
    y_1 = random.randint(0, 1) #znak pierwszej liczby
    y_2 = random.randint(0, 1) #znak drugiej liczby

    N = 26 #największa liczba całkowita jaka może się wylosować
    M = 15 #największy mianownik jaki może się wylosować
    LICZBY = []
    for i in range(N):
        LICZBY.append(i+1)

    m1 = random.randint(2, M) #mianownik
    m2 = random.randint(2, M) #mianownik

    l_1 = 0
    while l_1 == 0 or l_1 % m1 == 0:
        l_1 = random.randint(-(m1 * M), m1*N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m1}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    l_2 = 0
    while l_2 == 0 or l_2 % m2 == 0:
        l_2 = random.randint(-(m2 * M), m2 * N)
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
    rozwiazanie = ''

    x = random.randint(0, 1) # 0 - mnożenie, 1 - dzielenie
    y_1 = random.randint(0, 1)  # znak pierwszej liczby
    y_2 = random.randint(0, 1)  # znak drugiej liczby

    N = 7  # największa liczba całkowita jaka może się wylosować
    M = 5  # największy mianownik jaki może się wylosować
    LICZBY = []
    for i in range(N):
        LICZBY.append(i + 1)

    m1 = random.randint(2, M)  # mianownik1

    l_1 = 0
    while l_1 == 0 or l_1 % m1 == 0:
        l_1 = random.randint(-(m1 * M), m1 * N)
    ulamek_1 = sympy.sympify(f'{l_1}/{m1}')
    tex1 = konwersja_ulamek_liczba_mieszana(ulamek_1)

    m2 = random.randint(2, M)  # mianownik2
    l_2 = 0
    while l_2 == 0 or l_2 % m2 == 0:
        l_2 = random.randint(-(m2 * M), m2 * N)
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



