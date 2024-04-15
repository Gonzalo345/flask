from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Página de inicio</h1>'

@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name = None, age = None):
    if name == None and age == None:
        return '<h1>Hola mundo!</h1>'
    elif age == None:
        return f'<h1>Hola, {name}!</h1>'
    else:   
        return f'<h1>Hola Mundo, {name} y tu edad es {age}!</h1>'
