from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    option = request.form['option']
    script_path = f'scripts/{option}.py'

    if not os.path.exists(script_path):
        return "Niepoprawna opcja", 400

    args = []

    if option == "stworz_dzialanie_ulamki":
        tryb = request.form.get('tryb', '1')
        ile = request.form.get('ile_przykladow', '26')
        args = [tryb, ile]

    elif option == "stworz_przyklad_pierwiastki":
        stopien = request.form.get('tryb', '2')
        ile = request.form.get('ile_przykladow', '26')
        trudnosc = request.form.get('trudnosc', '1')
        args = [stopien, ile, trudnosc]


    if os.name == "nt":
        python_executable = os.path.join(".venv", "Scripts", "python.exe")
    else:
        python_executable = os.path.join(".venv", "bin", "python")
    result = subprocess.run([python_executable, script_path, *args], capture_output=True, text=True)

    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)

    pdf_path = f'output/zadania.pdf'
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    else:
        return "PDF nie został wygenerowany", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
