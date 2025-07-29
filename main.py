from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    print("== generate() został wywołany ==")
    option = request.form['option']
    script_path = f'scripts/{option}.py'

    if not os.path.exists(script_path):
        return "Niepoprawna opcja", 400

    # Wykonaj skrypt (który generuje PDF)
    print(f"URUCHAMIAM: {script_path}")
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    print("==== stdout ====")
    print(result.stdout)
    print("==== stderr ====")
    print(result.stderr)

    pdf_path = f'output/{option}.pdf'
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    else:
        return "PDF nie został wygenerowany", 500

if __name__ == '__main__':
    app.run(debug=True)



# import tkinter as tk
# from tkinter import messagebox
#
# from scripts import stworz_uklad_rownan
# from scripts import stworz_rownanie_nierownosc
# from scripts import stworz_dzialanie_ulamki
#
# def show_dropdown_window(title, options_dict, callback):
#     win = tk.Toplevel(root)
#     win.title(title)
#     win.geometry("350x200")
#
#     tk.Label(win, text=title, font=("Arial", 12)).pack(pady=10)
#
#     var = tk.StringVar(win)
#     var.set(list(options_dict.keys())[0])
#
#     option_menu = tk.OptionMenu(win, var, *options_dict.keys())
#     option_menu.pack(pady=10)
#
#     def submit():
#         selected_label = var.get()
#         selected_value = options_dict[selected_label]
#         win.destroy()
#         callback(selected_value)
#
#     tk.Button(win, text="OK", command=submit).pack(pady=10)
#
# def generuj_uklad():
#     def kontynuuj_z_generowaniem(tryb):
#         def wybierz_liczbe_zmiennych():
#             liczby = { "2 zmienne": 2, "3 zmienne": 3 }
#             def kontynuuj(liczba_zmiennych):
#                 stworz_uklad_rownan.generuj_pdf(tryb=tryb, liczba_zmiennych=liczba_zmiennych)
#                 messagebox.showinfo("Sukces", "Wygenerowano PDF z układami równań!")
#             show_dropdown_window("Liczba zmiennych", liczby, kontynuuj)
#         wybierz_liczbe_zmiennych()
#
#     tryby = {
#         "Łatwe": 1,
#         "Trudne": 2
#     }
#     show_dropdown_window("Tryb układów równań", tryby, kontynuuj_z_generowaniem)
#
# def generuj_rownania():
#     tryby = {
#         "Łatwe kwadratowe": 1,
#         "Trudne kwadratowe": 2,
#         "Równanie 3-go stopnia": 3
#     }
#
#     def kontynuuj(tryb):
#         stworz_rownanie_nierownosc.generuj_pdf(tryb=tryb)
#         messagebox.showinfo("Sukces", "Wygenerowano PDF z równaniami/nierównościami!")
#
#     show_dropdown_window("Tryb równań", tryby, kontynuuj)
#
# def generuj_ulamki():
#     tryby = {
#         "Dodawanie i odejmowanie (łatwe)": 1,
#         "Dodawanie i odejmowanie (trudne)": 2,
#         "Mnożenie i dzielenie": 3
#     }
#
#     def kontynuuj(tryb):
#         stworz_dzialanie_ulamki.generuj_pdf(tryb=tryb)
#         messagebox.showinfo("Sukces", "Wygenerowano PDF z działaniami na ułamkach!")
#
#     show_dropdown_window("Tryb działań na ułamkach", tryby, kontynuuj)
#
# # Główne okno
# root = tk.Tk()
# root.title("Generator zadań matematycznych")
# root.geometry("400x250")
#
# label = tk.Label(root, text="Wybierz typ zadań do wygenerowania:", font=("Arial", 12))
# label.pack(pady=20)
#
# tk.Button(root, text="Układy równań", command=generuj_uklad, width=30).pack(pady=5)
# tk.Button(root, text="Równania / Nierówności", command=generuj_rownania, width=30).pack(pady=5)
# tk.Button(root, text="Działania na ułamkach", command=generuj_ulamki, width=30).pack(pady=5)
# tk.Button(root, text="Zamknij", command=root.destroy, width=30).pack(pady=20)
#
# root.mainloop()
