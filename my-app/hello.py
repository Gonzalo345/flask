from flask import Flask, render_template

app = Flask(__name__)
# Filtros personalizados

from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    name = 'Gonzalo'
    friends = ['Matias', 'Agustin', 'Agusto']
    date = datetime.now()
    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        date = date)

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
from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'