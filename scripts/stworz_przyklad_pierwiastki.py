from generate_pdf import pdf
from przyklad_pierwiastek import *

def generuj_pdf(stopien=2, trudnosc=1, ile_przykladow=26):


    output = ''
    output += '\\begin{enumerate}\n'
    output += '\\renewcommand{\labelenumi}{\\alph{enumi})}\n'
    rozwiazania = []
    while True:
        if stopien == 2:
            dzialanie, r = tworz_dzialanie_0(trudnosc)
        else:
            dzialanie, r = tworz_dzialanie_1(difficulty=trudnosc, degree=stopien)

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