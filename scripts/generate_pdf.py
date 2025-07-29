import os
import shutil


def pdf(latex_text, output_dir, temp_dir, file_name):


    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)


    output=''
    output+='\\documentclass[24 pt]{article}\n'
    output+='\\usepackage[cp1250]{inputenc}\n'
    output+='\\usepackage[T1]{fontenc}\n'
    output+='\\usepackage{amsmath}\n'
    output+='\\usepackage{amssymb}\n'
    output+='\\pagestyle{empty}\n'
    output+='\\begin{document}\n'

    output+= latex_text

    output += '\\end{document}'


    # Ścieżka do pliku .tex
    tex_path = os.path.join(temp_dir, f"{file_name}.tex")
    with open(tex_path, "w", encoding="cp1250") as f:
        f.write(output)

    # Uruchom pdflatex w katalogu tymczasowym
    os.system(f"cd {temp_dir} && pdflatex -interaction=nonstopmode {file_name}.tex")

    # Przenieś PDF do katalogu docelowego
    pdf_src = os.path.join(temp_dir, f"{file_name}.pdf")
    pdf_dest = os.path.join(output_dir, f"{file_name}.pdf")
    if os.path.exists(pdf_src):
        shutil.move(pdf_src, pdf_dest)
        print(f"Plik PDF zapisany w: {pdf_dest}")
    else:
        print("Nie udało się wygenerować pliku PDF.")

    # (Opcjonalnie) wyczyść katalog tymczasowy z plików innych niż .pdf
    # shutil.rmtree(temp_dir)

