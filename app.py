import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def bible():  # put application's code here
    pesquisa = 'João+3:16?translation=almeida'
    resposta = requests.get('https://bible-api.com/' + pesquisa).json()['reference'],['text']

    return render_template('search.html', resposta=resposta)


if __name__ == '__main__':
    app.run()
