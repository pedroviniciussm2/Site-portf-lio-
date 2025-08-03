from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

projetos = [
    {"titulo": "Projeto 1", "descricao": "Descrição breve do projeto 1.", "link": "#"},
    {"titulo": "Projeto 2", "descricao": "Descrição breve do projeto 2.", "link": "#"},
    {"titulo": "Projeto 3", "descricao": "Descrição breve do projeto 3.", "link": "#"},
]

@app.route("/")
def home():
    return render_template("index.html", ano=datetime.now().year, projetos=projetos)

if __name__ == "__main__":
    app.run(debug=True)
