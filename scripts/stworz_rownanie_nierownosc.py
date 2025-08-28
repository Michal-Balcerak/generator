from r_kwadratowe1 import tworz_rownanie_1
from r_kwadratowe2 import tworz_rownanie_2
from r_stopnia_3 import tworz_rownanie_3, tworz_rownanie_3b
from nierownosc_kwadratowa1 import tworz_nierownosc_1
from r_liniowe import *
from generate_pdf import pdf

def generuj_pdf(tryb=1,ile_przykladow=26):

    output=''
    if tryb == 1:
        funkcja = tworz_rownanie_1
    elif tryb ==2:
        funkcja = tworz_rownanie_2
    elif tryb ==3:
        funkcja = tworz_nierownosc_1
    elif tryb==4:
        funkcja = tworz_rownanie_3
    elif tryb==5:
        funkcja = tworz_rownanie_3b
    else:
        funkcja = tworz_rownanie_0

    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'

    rozwiazania = []

    for i in range(ile_przykladow):

        output += '\\item\n'
        output += '$'
        x = funkcja()
        output += x[0]
        rozw = x[1]
        output += '$\\\\'
        if rozw:
            if rozw == 'nierownosc':
                rozwiazania.append(f'${x[2]}$')
                # output += '$'
                # output += x[2]
                # output += '$'

            if len(rozw) == 2 and rozw[0] == rozw[1]:
                v = ''
                v += "$x_{0}="
                v += f"{rozw[0]}$"
                rozwiazania.append(v)
                # rozwiazania.append("$x_{0}=")
                # rozwiazania.append(f"{x[1][0]}$")
                # output += "$x_{0}="
                # output += f"{x[1][0]}$"
            elif rozw != 'nierownosc':
                v = ''
                for j, k in enumerate(rozw):
                    # output += f'$x_{j+1}={k}$, '
                    if len(rozw)==1:
                        v += f'$x={k}$'
                    else:
                        v += f'$x_{j+1}={k}$, '
                rozwiazania.append(v)
        elif not rozw:
            rozwiazania.append("$x\in\emptyset$")
    output += '\\end{enumerate}\n'

    output += "Rozwiązania:"
    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'

    for i in rozwiazania:
        output += '\\item\n'
        output += i

    output += '\\end{enumerate}\n'

    output_dir = "zadania"
    temp_dir = "temp_build"
    file_name = f"równania"


    pdf(latex_text=output, output_dir=output_dir, temp_dir=temp_dir, file_name=file_name)

if __name__ == "__main__":
    import sys
    try:
        ile = int(sys.argv[1]) if len(sys.argv) > 1 else 26
        tryb = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    except ValueError:
        tryb, ile = 1, 26

    generuj_pdf(tryb=tryb, ile_przykladow=ile)