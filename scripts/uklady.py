import random


def stworz_uklad(n):
    oznaczenia = []
    out = ''
    zmienne = []

    if n == 2:
        oznaczenia = ['x', 'y']
    elif n == 3:
        oznaczenia = ['x', 'y', 'z']
    else:
        for i in range(n):
            oznaczenia.append(f'x_{i+1}')

    for i in range(n):
        x = random.randint(-9, 9)
        while x==0:
            x = random.randint(-9, 9)
        zmienne.append(x)

    for i in range(n):
        suma = 0
        z = 0
        for j, k in enumerate(zmienne):
            a = random.randint(-9, 9)
            while a == 0:
                a = random.randint(-9, 9)

            if z and j and a > 0:
                out += '+'
            if a == -1:
                out += '-'
            elif a != 1:
                out += str(a)
            out += oznaczenia[j]
            z = 1
            suma = suma + a * k

        out += '='
        out += str(suma)
        out += '\\\\'
        out += '\n'


    rozwiazania = []
    for i, j in enumerate(zmienne):
        rozwiazania.append((oznaczenia[i], j))

    return out, rozwiazania
