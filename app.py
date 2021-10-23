import random

import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)

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



@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/temas/')
def temas():
    return render_template('temas.html')

@app.route('/resp_search/')
def resp_search():
    return render_template('resp_search.html')


@app.route('/list_temas/')
def list_temas():
    list_temas = {'#1':
                        ['https://www.youtube.com/embed/Aaded3mkJQs', 'Lidando com Desanimo', 'Lidar com o desânimo é um desafio de todos, aqui temos uma mensagem de ânimo.'],
                  '#2':
                        ['https://www.youtube.com/embed/u8Jp59weTS4', 'Não andeis ansiosos', 'Um grande mal do século, veja conselhos para não ficar ansioso.'],
                  '#3':
                        ['https://www.youtube.com/embed/N4CzAwNQXPg', 'Transformando a tristeza em alegria', 'Está triste ou angústiado?! Veja esta mensagem'],
                 }
    return render_template('temas.html', list_temas=list_temas)


@app.route('/')
def list_dev():

    with open('./templates/listPhoto.json', encoding='utf-8') as f:
        list_dev = json.load(f)

    rangeselected = random.randrange(0, 3, 1)

    return render_template('index.html', list_dev=list_dev[rangeselected])

if __name__ == '__main__':
    app.run()
