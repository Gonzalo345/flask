from flask import Blueprint, render_template
from todor.auth import login_required
from .models import Todo, User
from todor import db

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)

@bp.route('/create')
def create():
    return render_template('todo/create.html')