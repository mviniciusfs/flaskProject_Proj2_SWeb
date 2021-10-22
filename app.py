import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/biblia/', methods=['GET', 'POST'])
def bible():  # put application's code here
#    pesquisa = 'João+3:16?translation=almeida'
    print("join1")
    livro = requests.args.get("livro") + "+"
    capitulo = requests.args.get("capitulo") + ":"
    versiculo = requests.args.get("versiculo") + "?translation=almeida"

#    livro = requests.args.get("livro")
#    capitulo = requests.args.get("capitulo")
#   versiculo = requests.args.get("versiculo")

#    livro = 'joão+'
#    capitulo = '3:'
#    versiculo = '16?translation=almeida'

    join = livro + capitulo + versiculo
    print("join")
    resposta = requests.get('https://bible-api.com/' + join)

#    resposta = requests.get('https://bible-api.com/' + pesquisa)

 #   retorno_livro = resposta.json()['reference']
 #   retorno_verso = resposta.json()['text']
 #   livro_vers = retorno_livro +' - '+ retorno_verso
    return pesquisa.text


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
