from generate_pdf import pdf
from wzory_skr_mnoz import *


#tryb
#1 - (4a+7b)^2
#2 - (3a-9b)(3a+9b)
#3 - (4a+7b)^3
#4 - (4a^3+7b^9)^2
#5 - (4a^3+7b^9)^3


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
            dzialanie, r = tworz_wzor1()
        elif tryb == 2:
            dzialanie, r = tworz_wzor2()
        elif tryb == 3:
            dzialanie, r = tworz_wzor1(degree=3)
        elif tryb == 4:
            dzialanie, r = tworz_wzor4(degree=2)
        elif tryb == 5:
            dzialanie, r = tworz_wzor4(degree=3)

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