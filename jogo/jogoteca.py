from flask import Flask,render_template

app = Flask(__name__)
class jogo :
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
@app.route('/inicio')
def ola():
    jogos1 = jogo('domm','fps','xbox')
    jogos2 = jogo('halo','fps','xbox')
    lista = [jogos1, jogos2 ]
    return render_template('index.html', titulo = 'jogos', jogos = lista)

app.run()
