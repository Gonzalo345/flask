from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/sing_in')
def register():
    return "Registrar usuraio"

@bp.route('/login')
def login():
    return "Login"
