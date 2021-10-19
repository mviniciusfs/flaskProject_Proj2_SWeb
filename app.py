import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/biblia/')
def bible():  # put application's code here
    pesquisa = 'João+3:16?translation=almeida'
    resposta = requests.get('https://bible-api.com/' + pesquisa)
    livro = resposta.json()['reference']
    verso = resposta.json()['text']
    livro_vers = livro+' - '+verso

    return render_template('search.html', livro_vers=livro_vers)


if __name__ == '__main__':
    app.run()
