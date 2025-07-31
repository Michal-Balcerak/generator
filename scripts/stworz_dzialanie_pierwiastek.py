from generate_pdf import pdf
from dzialania_pierwiastki import *

# 1 - mnożenie
# 2 - dodawanie i odejmowanie

def generuj_pdf(tryb=1, ile_przykladow=26, stopien=2):

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
            dzialanie, r = tworz_dzialanie_1(degree=stopien)
        elif tryb == 2:
            dzialanie, r = tworz_dzialanie_2(degree=stopien)
        # elif tryb == 3:
        #     dzialanie, r = tworz_dzialanie_3()
        output += dzialanie
        output += '$\\\\'
        if r:
            rozwiazania.append(r)

    output += '\\end{enumerate}\n'

    if rozwiazania:
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
    try:
        stopien = int(sys.argv[1]) if len(sys.argv) > 1 else 2
        ile = int(sys.argv[2]) if len(sys.argv) > 2 else 26
        tryb = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    except ValueError:
        stopien, ile, tryb = 2, 26, 1

    generuj_pdf(tryb=tryb, ile_przykladow=ile, stopien=stopien)