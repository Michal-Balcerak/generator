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
