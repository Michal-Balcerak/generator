from generate_pdf import pdf
from dzialania_ulamki import *

# 1 - dodawanie i odejmowanie, ten sam mianownik
# 2 - dodawanie i odejmowanie, dowolny mianownik
# 3 - mnożenie i dzielenie
# 4 - dziesietne - dodawanie i odejmowanie
# 5 - dziesietne - mnożenie



def generuj_pdf(tryb=1, ile_przykladow=26):

    output = ''

    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'


    rozwiazania = []
    for i in range(ile_przykladow):
        dzialanie = ''
        r = ''
        output += '\\item\n'
        output += '$'
        if tryb == 1:
            dzialanie, r = tworz_dzialanie_1()
        elif tryb == 2:
            dzialanie, r = tworz_dzialanie_2()
        elif tryb == 3:
            dzialanie, r = tworz_dzialanie_3()
        elif tryb == 4:
            dzialanie, r = tworz_dzialanie_4()
        elif tryb == 5:
            dzialanie, r = tworz_dzialanie_5()
        # elif tryb == 6:
        #     dzialanie, r = tworz_dzialanie_6()
        output += dzialanie
        output += '$\\\\'
        rozwiazania.append(r)

    output += '\\end{enumerate}\n'

    output += 'Rozwiązania:'
    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'
    for i in range(ile_przykladow):
        output += '\\item\n'
        output += '$'
        output += rozwiazania[i]
        output += '$'
        # output += '$\\newline'
    output += '\\end{enumerate}\n'

    output_dir = "output"
    temp_dir = "temp_build"
    file_name = f"zadania"


    pdf(latex_text=output, output_dir=output_dir, temp_dir=temp_dir, file_name=file_name)

if __name__ == "__main__":
    import sys
    tryb = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    ile = int(sys.argv[2]) if len(sys.argv) > 2 else 26
    generuj_pdf(tryb=tryb, ile_przykladow=ile)

