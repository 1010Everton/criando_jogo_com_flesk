from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return 'index.html'

app.run()
