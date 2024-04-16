from flask import Flask, render_template

app = Flask(__name__)
# Filtros personalizados

@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

#@app.add_template_global
def repeat(s, n):
    return s * n

app.add_template_global(repeat, 'repeat')
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
        date = date,
        )

@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
    my_data = {
        'name': name,
        'age' : age,
        'email' : email
    }
    return render_template('hello.html',data = my_data)

from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'