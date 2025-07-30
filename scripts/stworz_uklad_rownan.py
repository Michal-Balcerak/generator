from uklady import stworz_uklad
from uklady2 import stworz_uklad2
from generate_pdf import pdf


def generuj_pdf(tryb=1, liczba_zmiennych=2, ile_przykladow=26):
    output=''

    output+='\\begin{enumerate}\n'
    output+='\\renewcommand{\labelenumi}{\\alph{enumi})}\n'


    for i in range(ile_przykladow):

        output+= '\\item\n'
        output += '\\begin{equation*}\n'
        output +='\\begin{cases}\n'
        ###
        if tryb == 1:
            x = stworz_uklad(liczba_zmiennych)
        else:
            x = stworz_uklad2(liczba_zmiennych)
        output += x[0]
        output += '\\end{cases}\n'
        output += '\\end{equation*}\n'
        # for j in x[1]:
        #     output += f'${j[0]}={j[1]}$, '

    output+='\\end{enumerate}\n'


    output_dir = "zadania"
    temp_dir = "temp_build"
    file_name = f"układy_równań"


    pdf(latex_text=output, output_dir=output_dir, temp_dir=temp_dir, file_name=file_name)
