from flask import Flask, render_template, request, redirect

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
def index():

    return render_template('lista.html', titulo='jogos', jogos=lista)

@app.route('/')
def novo():
    return render_template('novo.html',titulo='novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/inicio')
@app.route('/login')
def login():
    return ('login.html')
@app.route('/autentica')
def autentica():
    if '123' == request.form ['senha']:
        return ('/')
    else:
        return ('/login')



app.run(debug=True)
