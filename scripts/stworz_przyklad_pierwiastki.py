from generate_pdf import pdf
from przyklad_pierwiastek import *

# Tryb
# 1 - stopien 2
# x - stopien x (3,4,5 - zalezy od trudnosci)
def generuj_pdf(tryb=1, trudnosc=1, ile_przykladow=26):


    output = ''
    output += '\\begin{enumerate}\n'
    output += '\\renewcommand{\labelenumi}{\\alph{enumi})}\n'
    rozwiazania = []
    while True:
        if tryb == 1:
            dzialanie, r = tworz_dzialanie_0(trudnosc)
        else:
            dzialanie, r = tworz_dzialanie_1(difficulty=trudnosc, degree=tryb)

        # jeśli unikalny przykład
        if r not in rozwiazania:
            output += '\\item\n'
            output += '$'
            output += dzialanie
            output += '$\\\\'
            rozwiazania.append(r)

        if len(set(rozwiazania))==ile_przykladow:
            break
    # if len(rozwiazania) == len(set(rozwiazania)):
    #     break
    # else:
    #     continue

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
    generuj_pdf()