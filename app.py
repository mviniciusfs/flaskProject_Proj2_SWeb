import requests
from flask import Flask, render_template, request

app = Flask(__name__)


#@app.route('/biblia/', methods=['GET', 'POST'])
#def bible():  # put application's code here
#    pesquisa = 'João+3:16?translation=almeida'
#    livro = request.args.get("livro"+ "+")
#    capitulo = request.args.get("capitulo" + ":")
#    versiculo = request.args.get("versiculo" + "?translation=almeida")

#    join = livro + capitulo + versiculo
#    url = 'http://bible-api.com/' + join
#    resposta = requests.get(url)

#    print(resposta)
#    return resposta.json()

@app.route('/searchValue/', methods=['GET'])
def getValue():
    livro = request.args.get("livro") + "+"
    capitulo = request.args.get("capitulo") + ":"
    versiculo = request.args.get("versiculo") + "?translation=almeida"
    url = 'http://bible-api.com/' + livro + capitulo + versiculo

    dados = requests.get(url)
    dadosJson = dados.json()
    return render_template("resp_search.html", dadosJson=dadosJson)


@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/')
def index_open():
    return render_template('index.html')

@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/temas/')
def temas():
    return render_template('temas.html')

@app.route('/resp_search/')
def resp_search():
    return render_template('resp_search.html')

if __name__ == '__main__':
    app.run()
