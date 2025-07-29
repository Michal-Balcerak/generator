from random import choices
import sympy as sp

from sympy import Integer, factorint
from math import prod


def simplified_nth_root_latex(number: int, degree: int) -> str:
    number = Integer(number)
    degree = Integer(degree)

    if number == 0:
        return "0"
    if number == 1:
        return "1"

    factors = factorint(number)

    outside = []
    inside = []

    for base, exp in factors.items():
        out_exp = exp // degree
        in_exp = exp % degree

        if out_exp > 0:
            outside.append(base ** out_exp)
        if in_exp > 0:
            inside.append(base ** in_exp)

    outside_product = prod(outside) if outside else 1

    if not inside:
        return str(outside_product)

    inside_product = prod(inside)

    if outside_product == 1:
        return rf"\sqrt[{degree}]{{{inside_product}}}"
    else:
        return rf"{outside_product}\sqrt[{degree}]{{{inside_product}}}"


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# sam pierwiastek - kwadratowy
def tworz_dzialanie_0(difficulty=1):

    difficulty = difficulty

    out = ''

    while True:
        exponents = []
        number = 1

        #liczba 2
        exponents.append(choices(list(range(10)), weights=[0.3, 0.3, 0.2, 0.15, 0.02, 0.01, 0.01, 0.05, 0.03, 0.02])[0])
        #liczba 3
        exponents.append(choices(list(range(7)), weights=[0.4, 0.3, 0.2, 0.05, 0.03, 0.01, 0.01])[0])
        #liczby 5 i 7
        exponents.append(choices(list(range(4)), weights=[0.4, 0.25, 0.3, 0.05])[0])
        exponents.append(choices(list(range(4)), weights=[0.5, 0.15, 0.3, 0.05])[0])


        if difficulty > 1:
            #liczby 11, 13, 17, 19
            for i in range(4):
                exponents.append(choices(list(range(3)), weights=[0.8, 0.1, 0.1])[0])
            if difficulty > 2:
                #liczby 23, 29, 31
                for i in range(3):
                    exponents.append(choices(list(range(3)), weights=[0.87, 0.1, 0.03])[0])

        # sprawdzenie czy przyklad nie jest trywialny
        if max(exponents)>1:
            for i, j in enumerate(exponents):
                number *= prime_numbers[i] ** j
            number = int(number)
        else:
            continue # ponowne generowanie


        # sprawdzenie czy liczba nie jest zbyt wielka
        if number < 1000:
            break
        else:
            continue

    out = out + f"\\sqrt{{{number}}}"


    #obliczanie wyniku:
    rozwiazanie = sp.sympify(sp.sqrt(number))
    rozwiazanie = sp.latex(rozwiazanie)

    return (out, rozwiazanie)

# sam pierwiastek - stopien wyzszy niz 2
def tworz_dzialanie_1(difficulty=1, degree=3):
    difficulty = difficulty
    degree = degree
    out = ''
    rozwiazanie = ''

    while True:
        exponents = []
        number = 1

        if degree < 10:
            # liczba 2
            weights = [0.45, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.003, 0.002, 0.001]
            weights[degree] += 0.3
            exponents.append(choices(list(range(10)), weights=weights)[0])
        if degree < 7:
            # liczba 3
            weights = [0.6, 0.1, 0.04, 0.02, 0.008, 0.005, 0.003]
            weights[degree] += 0.3
            exponents.append(choices(list(range(7)), weights=weights)[0])
        else:
            exponents.append(choices(list(range(3)), weights=[0.7,0.28,0.02])[0])
        if degree < 4:
            # liczby 5 i 7
            weights = [0.75, 0.09, 0.0005, 0.0005]
            weights[degree] += 0.19
            exponents.append(choices(list(range(4)), weights=weights)[0])
            exponents.append(choices(list(range(4)), weights=weights)[0])
        else:
            exponents.append(choices(list(range(3)), weights=[0.80, 0.195, 0.005])[0])
            exponents.append(choices(list(range(2)), weights=[0.9, 0.1])[0])


        if difficulty > 1:

            # liczby 11, 13, 17, 19
            if degree < 4:
                for i in range(4):
                    weights = [0.9, 0.08, 0.0005, 0.0005]
                    weights[degree] += 0.07
                    exponents.append(choices(list(range(4)), weights=weights)[0])
            else:
                weights = [0.93, 0.07]
                for i in range(4):
                    exponents.append(choices(list(range(2)), weights=weights)[0])
        # if difficulty > 2:
        #     # liczby 23, 29, 31
        #     if degree < 4:
        #         for i in range(3):
        #             weights = [0.96, 0.05, 0.0005, 0.0005]
        #             weights[degree] += 0.04
        #             exponents.append(choices(list(range(4)), weights=weights)[0])
        #     else:
        #         weights = [0.99, 0.01]
        #         for i in range(3):
        #             exponents.append(choices(list(range(2)), weights=weights)[0])

        # sprawdzenie czy przyklad nie jest trywialny
        if max(exponents) >= degree:
            for i, j in enumerate(exponents):
                number *= prime_numbers[i] ** j
            number = int(number)
        else:
            continue  # ponowne generowanie

        #sprawdzenie czy liczba nie jest zbyt wielka
        if number < 40**(degree*0.7):
            break
        else:
            continue

    out = out + f"\\sqrt[{degree}]{{{number}}}"

    # obliczanie wyniku:
    # wyrażenie: number ** (k / degree)
    #expr = sp.Pow(number, sp.Rational(3, degree))  # to będzie np. 2**(3/4)

    # --- Automatyczne wyciągnięcie wykładnika:
    # if isinstance(expr, sp.Pow):
    #     base = expr.base
    #     exponent = expr.exp
    #
    #     if isinstance(exponent, sp.Rational) and exponent.q == degree:
    #         k = exponent.p  # licznik
    #         # teraz budujesz wyrażenie w postaci: (√[degree]{number})^k
    #         rozwiazanie = sp.root(base, degree) ** k
    #         rozwiazanie = sp.latex(rozwiazanie, root_notation=True)

    # rozwiazanie = sp.root(number, degree)
    # rozwiazanie = sp.latex(rozwiazanie)

    rozwiazanie = simplified_nth_root_latex(number, degree)

    return (out, rozwiazanie)