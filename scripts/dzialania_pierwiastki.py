from random import choices

from sympy import root, simplify, Integer, factorint

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def simplify_nth_root_expr(a, b, c, d, n):
    # Oblicz wyrażenie
    expr = Integer(a) * root(b, n) * Integer(c) * root(d, n)
    simplified = simplify(expr)

    # Oddziel część całkowitą i pierwiastek
    coeff, rad = simplified.as_coeff_Mul()

    # Jeśli rad zawiera pierwiastek, wyodrębnij podstawę i stopień
    if rad.is_Pow and rad.exp.is_Rational and rad.exp.q == n:
        base = rad.base
        x = coeff
        y = base
    else:
        x = simplified
        y = 1  # nie ma pierwiastka

    return x, y


def simplify_to_radical_form(a, b, c, d, n):
    # Połącz wszystko razem
    coeff = Integer(a) * Integer(c)
    under_root = Integer(b) * Integer(d)

    # Łączna potęga pod pierwiastkiem
    radicand = under_root

    # Rozłóż radicand na czynniki pierwsze
    factors = factorint(radicand)

    # Wyciągnij z pierwiastka co się da
    outside = 1
    inside = 1
    for base, exp in factors.items():
        q, r = divmod(exp, n)
        outside *= base ** q
        if r > 0:
            inside *= base ** r

    x = coeff * outside
    y = inside

    return x, y


def extract_radical_parts(k, radicand, n):
    radicand = Integer(radicand)
    factors = factorint(radicand)
    outside = 1
    inside = 1
    for base, exp in factors.items():
        q, r = divmod(exp, n)
        outside *= base ** q
        if r > 0:
            inside *= base ** r
    return Integer(k) * outside, Integer(inside)


def simplify_sum_of_radicals(a, b, c, d, n):
    # Upraszczamy każde wyrażenie osobno
    x1, y1 = extract_radical_parts(a, b, n)
    x2, y2 = extract_radical_parts(c, d, n)

    # Jeśli pierwiastki są takie same, można dodać współczynniki
    if y1 == y2:
        return x1 + x2, y1
    else:
        return None, None  # nie da się sprowadzić do wspólnego pierwiastka


def generate_number_under_root(degree):
    while True:
        exponents = []
        number = 1
        # liczby 2,3,5,7
        for i in range(4):
            weights = [10, 3, 1, 0.5, 0.1]
            weights[degree] *= 0.3
            exponents.append(choices(list(range(5)), weights=weights)[0])

        # sprawdzenie czy przyklad nie jest trywialny
        if max(exponents) > 1:
            for i, j in enumerate(exponents):
                number *= prime_numbers[i] ** j
            number = int(number)
        else:
            continue  # ponowne generowanie

        # sprawdzenie czy liczba nie jest zbyt wielka
        if number < 100:
            break

    return number

# mnożenie - współczynniki całkowite, wszystko dodatnie
# a\sqrt{b}*c\sqrt{d}
# mozliwe stopnie: 2, 3, 4
def tworz_dzialanie_1(degree=2):
    out = ''
    rozwiazanie = ''

    a = choices(list(range(12)), weights=[0,10,7,5,3,3,3,3,3,3,3,3])[0]
    c = choices(list(range(12)), weights=[0,10,7,5,3,3,3,3,3,3,3,3])[0]

    b = generate_number_under_root(degree)
    d = generate_number_under_root(degree)

    if a!=1:
        out += str(a)

    if degree > 2:
        out = out + f"\\sqrt[{degree}]{{{b}}}"
    else:
        out = out + f"\\sqrt{{{b}}}"
    out += '\\cdot'
    if c!=1:
        out += str(c)
    if degree >2:
        out = out + f"\\sqrt[{degree}]{{{d}}}"
    else:
        out = out + f"\\sqrt{{{d}}}"

    x, y = simplify_to_radical_form(a, b, c, d, degree)

    if y == 1:
        rozwiazanie += str(x)
    else:
        if x != 1:
            rozwiazanie += str(x)
        if degree > 2:
            rozwiazanie += f'\\sqrt[{degree}]{{{y}}}'
        else:
            rozwiazanie += f'\\sqrt{{{y}}}'

    return (out, rozwiazanie)




motifs = [2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30]
def generate_number_with_motif(motif, degree):
    while True:
        exponents = []

        # liczby 2,3,5
        weights = [1, 0, 0, 0, 0]
        weights[degree] = 1
        for i in range(3):
            exponents.append(choices(list(range(5)), weights=weights)[0])

        # liczby 7,11,13
        weights = [1, 0, 0, 0, 0]
        weights[degree] = 0.3
        for i in range(3):
            exponents.append(choices(list(range(5)), weights=weights)[0])

        # liczby 17,19,23,29
        weights = [1, 0, 0, 0, 0]
        weights[degree] = 0.1
        for i in range(4):
            exponents.append(choices(list(range(5)), weights=weights)[0])

        number = 1
        for i, j in enumerate(exponents):
            number *= prime_numbers[i] ** j
        number = int(number)

        result = motif * number
        if result < 200:
            break
    return result


# dodawanie i odejmowanie
# maks. stopien = 4
#+-a\sqrt{b}+=c\sqrt{d}
def tworz_dzialanie_2(degree=2):
    out = ''
    rozwiazanie = ''

    a = 1
    b = 1
    c = -1
    d = 1
    # unikamy trywialnych działań typu 3sqrt{2}-3sqrt{2}
    while (a,b) == (-c,d):
        weights = [3 for i in range(21)]
        weights[7], weights[13] = 5, 5
        weights[8], weights[12] = 7, 7
        weights[9], weights[11] = 10, 10
        weights[10] = 0

        a = choices(list(range(-10,11)), weights=weights)[0]
        c = choices(list(range(-10,11)), weights=weights)[0]

        motif = choices(motifs)[0]

        b = generate_number_with_motif(motif=motif, degree=degree)
        d = generate_number_with_motif(motif=motif, degree=degree)

    if a==-1:
        out += '-'
    elif a != 1:
        out+= str(a)
    if degree > 2:
        out = out + f"\\sqrt[{degree}]{{{b}}}"
    else:
        out = out + f"\\sqrt{{{b}}}"

    if c==-1:
        out += '-'
    else:
        if c > 0:
            out += '+'
        if c != 1:
            out+=str(c)

    if degree > 2:
        out = out + f"\\sqrt[{degree}]{{{d}}}"
    else:
        out = out + f"\\sqrt{{{d}}}"

    x, y = simplify_sum_of_radicals(a, b, c, d, degree)

    if x == 0:
        rozwiazanie += '0'
    else:
        if x != 1:
            if x == -1:
                rozwiazanie += '-'
            else:
                rozwiazanie += str(x)
        if degree > 2:
            rozwiazanie += f'\\sqrt[{degree}]{{{y}}}'
        else:
            rozwiazanie += f'\\sqrt{{{y}}}'

    return (out, rozwiazanie)

