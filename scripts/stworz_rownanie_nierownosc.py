from r_kwadratowe1 import tworz_rownanie_1
from r_kwadratowe2 import tworz_rownanie_2
from r_stopnia_3 import tworz_rownanie_3
from nierownosc_kwadratowa1 import tworz_nierownosc_1
from generate_pdf import pdf

def generuj_pdf(tryb=1,ile_przykladow=26):

    output=''
    if tryb == 1:
        funkcja = tworz_rownanie_1
    elif tryb ==2:
        funkcja = tworz_rownanie_2
    elif tryb ==3:
        funkcja = tworz_rownanie_3
    else:
        funkcja = tworz_nierownosc_1

    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'

    rozwiazania = []

    for i in range(ile_przykladow):

        output += '\\item\n'
        output += '$'
        x = funkcja()
        output += x[0]
        output += '$\\\\'
        if x[1]:
            if x[1] == 'nierownosc':
                rozwiazania.append(f'${x[2]}$')
                # output += '$'
                # output += x[2]
                # output += '$'

            if len(x[1]) == 2 and x[1][0] == x[1][1]:
                v = ''
                v += "$x_{0}="
                v += f"{x[1][0]}$"
                rozwiazania.append(v)
                # rozwiazania.append("$x_{0}=")
                # rozwiazania.append(f"{x[1][0]}$")
                # output += "$x_{0}="
                # output += f"{x[1][0]}$"
            elif x[1] != 'nierownosc':
                v = ''
                for j, k in enumerate(x[1]):
                    # output += f'$x_{j+1}={k}$, '
                    v += f'$x_{j+1}={k}$, '
                rozwiazania.append(v)
        elif not x[1]:
            rozwiazania.append("$x\in\emptyset$")
    output += '\\end{enumerate}\n'

    output += "Rozwiązania:"
    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'

    for i in rozwiazania:
        output += '\\item\n'
        output += i

    output += '\\end{enumerate}\n'

    output_dir = "output"
    temp_dir = "temp_build"
    file_name = "zadania"


    pdf(latex_text=output, output_dir=output_dir, temp_dir=temp_dir, file_name=file_name)

if __name__ == "__main__":
    import sys
    try:
        ile = int(sys.argv[1]) if len(sys.argv) > 1 else 26
        tryb = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    except ValueError:
        tryb, ile = 1, 26

    generuj_pdf(tryb=tryb, ile_przykladow=ile)