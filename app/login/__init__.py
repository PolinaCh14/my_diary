from flask import Blueprint

bp = Blueprint('login', __name__,static_folder='static', static_url_path='/static')

from app.login import routes