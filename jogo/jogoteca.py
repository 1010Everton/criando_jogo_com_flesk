from flask import Flask,render_template,request

app = Flask(__name__)
class Jogo :
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogos1 = Jogo('domm','fps','xbox')
jogos2 = Jogo('halo','fps','xbox')
lista = [jogos1, jogos2]
@app.route('/inicio')
def apresenta():

    return render_template('index.html', titulo='jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html',titulo='novo jogo')

@app.route('/criar')
def jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('novo.html',titulo='jogos',jogos=lista)

app.run()
