from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY ='dev'
)
# Filtros personalizados

@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

@app.add_template_global
def repeat(s, n):
    return s * n

from datetime import datetime

@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello', name = 'Gonzalo', age = '37'))
    print(url_for('code', code = 'print("Hola mundo 3")'))
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


# crear formulario wtform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario: ", validators= [DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators=[DataRequired(),Length(min=4, max=25)])
    submit = SubmitField("Registrar: ")
# Registrar usario
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Nombre de usuario: {username}, Contraseña: {password}" 
    #if request.method == 'POST':
    #    username = request.form['username']
    #    password = request.form['password']
    #    if len(username) >= 8 and len(username) <= 25 and len(password) >= 8 and len (password) <= 40:
    #        return f"Nombre de usuario: {username}, Contraseña: {password}"
    #    else:
    #        error = """"Nobre de usuario tiene que tener entre 8 y 25 caracteres y 
    #        la contraseña debe tener entre 8 y 40 caracteres.
    #        """
    #        return render_template('auth/register.html', form = form, error = error)
    
    return render_template('auth/register.html', form = form)