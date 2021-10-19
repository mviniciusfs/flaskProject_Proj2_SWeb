import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/biblia/')
def bible():  # put application's code here
#    pesquisa = 'João+3:16?translation=almeida'

    livro = requests.args.get("livro" + "+")
    capitulo = requests.args.get("capitulo" + ":")
    versiculo = requests.args.get("versiculo")

    resposta = requests.get('https://bible-api.com/' + livro + capitulo + versiculo)

    retorno_livro = resposta.json()['reference']
    retorno_verso = resposta.json()['text']
    livro_vers = retorno_livro +' - '+ retorno_verso

    return render_template('search.html', livro_vers=livro_vers)


if __name__ == '__main__':
    app.run()
