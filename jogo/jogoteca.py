from flask import Flask,render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['good of war', 'the last of us', 'horizon']
    return render_template('index.html', titulo = 'jogos', jogos = lista)

app.run()
