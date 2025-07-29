import random
import sys
from .funkcje import NWD



def stworz_uklad2(n):
    oznaczenia = []
    out = ''
    zmienne = []

    if n == 2:
        oznaczenia = ['x', 'y']
    elif n == 3:
        oznaczenia = ['x', 'y', 'z']
    else:
        sys.exit()
        # for i in range(n):
        #     oznaczenia.append(f'x_{i+1}')

    for i in range(n):
        x = random.randint(-9, 9)
        while x==0:
            x = random.randint(-9, 9)
        zmienne.append(x)

    for i in range(n):
        ulamki = []
        z = 0
        for j in range(2):
            a = random.randint(-10, 10)
            while a == 0:
                a = random.randint(-9, 9)

            wspolczynniki = []
            for k in range(n+1):
                x = random.randint(-10, 10)
                while x == 0:
                    x = random.randint(-9, 9)
                wspolczynniki.append(x)

            jest_niezerowy = False
            for k in wspolczynniki:
                if k:
                    jest_niezerowy = True

            if a and jest_niezerowy:
                if z and a > 0:
                    out += '+'
                elif a < 0:
                    out += '-'
                z = 1
                if a != 1 and a != -1:
                    out += "\\frac{"


                elif a == -1:
                    out += "("


                q = 0
                for h, s in enumerate(wspolczynniki):
                    if q and s > 0:
                        out += '+'
                    if s:
                        if h < len(oznaczenia):
                            if s != 1 and s != -1:
                                out += str(s)
                            elif s == -1:
                                out += "-"
                            out += oznaczenia[h]

                        else:
                            out += str(s)
                        q = 1


                if a != 1 and a != -1:
                    out += "}{"
                    out += str(abs(a))
                    out += "}"
                elif a == -1:
                    out += ")"

                licznik = 0
                for x, y in enumerate(zmienne):
                    licznik = licznik + y*wspolczynniki[x]
                licznik += wspolczynniki[-1]

                ulamki.append([licznik, a])


        out += '='
        y = 0
        if len(ulamki) == 2:
            a = ulamki[0][0]
            b = ulamki[0][1]
            c = ulamki[1][0]
            d = ulamki[1][1]

            ulamek = [a*d+b*c, b*d]  #[licznik mianownik]

            x = ulamek[0]
            y = ulamek[1]


        elif len(ulamki)==1:
            x = ulamki[0][0]
            y = ulamki[0][1]

        else:
            x = 0
        if x == 0:
            out += "0"
        elif y:
            if y != 1 and y != -1:
                minus = False
                if x * y < 0:
                    minus = True
                x = abs(x)
                y = abs(y)
                z = x // y
                r = x - y * z
                # liczba_mieszana = [z, r, y]  # [calosci, licznik, mianownik]

                if minus:
                    out += "-"
                if z:
                    out += str(z)
                if r:
                    m = NWD(r, y)
                    r = int(r/m)
                    y = int(y/m)
                    out += "\\frac{"
                    out += str(r)
                    out += "}{"
                    out += str(y)
                    out += "}"


            else:
                 out += str(x)
        out += '\\\\'
        out += '\n'
    rozwiazania = []
    for i, j in enumerate(zmienne):
        rozwiazania.append((oznaczenia[i], j))

    return out, rozwiazania
