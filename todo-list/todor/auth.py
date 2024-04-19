from flask import (
    Blueprint, render_template, request, redirect, flash, url_for, session, g
    )

from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/sing_in', methods = ('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, generate_password_hash(password))

        error = None

        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya estar registrado'
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_name = User(username, generate_password_hash(password))

        error = None
        # Validar los datos
        user = User.query.filter_by(username = username).first()
        if user == None:
            error = 'Nombre de usuario incoorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta'

        # Iniciar sesion 
        if error == None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))
                
        flash(error)

    return render_template('auth/login.html')

# Se ejecuta en cada peticion
@bp.before_app_request 
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id == None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
    print (g.user)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

import functools
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view