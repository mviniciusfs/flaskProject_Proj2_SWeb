import requests
from flask import Flask, render_template, request

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
    list_dev = {'#1':
                        ['https://i.picsum.photos/id/1018/3914/2935.jpg?hmac=3N43cQcvTE8NItexePvXvYBrAoGbRssNMpuvuWlwMKg', 'A Melhor Maneira de Passar o Tempo', 'É simples: quanto mais tempo você passa com Deus, mais você se conecta ao Seu poder. Davi nos diz que é no esconderijo da presença de Deus que somos protegidos (ver Salmos 91:1-2). Quando passamos tempo na presença de Deus, em oração, e com a Sua Palavra, estamos nesse lugar. O esconderijo é um lugar maravilhoso de paz e descanso! É poderoso pensar que a grandiosidade da presença de Deus está disponível a nós como cristãos. Tendo isso em mente, por que cargas d’água não iríamos querer passar tempo com Deus? Até Jesus se levantava cedo pela manhã para estar a sós com Deus. Ele conhecia o valor de estar na presença de Deus. Nós extraímos força e sabedoria do simples fato de apenas estarmos com Deus!'],
                '#2':
                        ['https://i.picsum.photos/id/1015/6000/4000.jpg?hmac=aHjb0fRa1t14DTIEBcoC12c5rAXOSwnVlaA5ujxPQ0I', 'Deus Entende Você', 'Qualquer pessoa que decida seguir a Deus passará por momentos em que será incompreendida pelas pessoas que não assumiram o mesmo compromisso. As pessoas sem fé não entendem as pessoas de fé! Sempre haverá aqueles que não saberão o que pensar a nosso respeito quando formos totalmente rendidos a Deus. As pessoas não sabiam o que pensar de Jesus também. Ninguém realmente o entendia, ou o chamado que estava sobre Sua vida, nem mesmo Sua própria família.'],
                '#3':
                        ['https://i.picsum.photos/id/1026/4621/3070.jpg?hmac=OJ880cIneqAKIwHbYgkRZxQcuMgFZ4IZKJasZ5c5Wcw', 'Vivendo Com Propósito', 'Deus é um Deus de propósito — Ele se move estrategicamente e trabalha para cumprir Seu plano perfeito. Deus deseja que Seus filhos sejam pessoas de propósito. Quanto mais próximos estivermos dele, com mais propósito viveremos. Jesus sempre soube do Seu propósito. Ele disse que Ele veio ao mundo para que pudéssemos ter vida e para que Ele pudesse destruir as obras do diabo (ver João 10:10; 1 João 3:8). No que se refere ao nosso propósito específico, ele varia de pessoa para pessoa e de um período da vida para o próximo, mas Deus tem um propósito geral no qual todos nós podemos escolher viver a cada dia.'],
                }


    return render_template('index.html',list_dev=list_dev)

if __name__ == '__main__':
    app.run()
