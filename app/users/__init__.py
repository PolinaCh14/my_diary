from flask import Blueprint

bp = Blueprint('users', __name__, static_folder='static', static_url_path='/static')

from app.users import routes