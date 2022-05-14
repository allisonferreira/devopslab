from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Teste 1"

if __name__ == '__main__':
    app.run()