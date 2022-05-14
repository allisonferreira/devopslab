from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Projeto criado por Allison no LAB Devops da Gaby"

if __name__ == '__main__':
    app.run()