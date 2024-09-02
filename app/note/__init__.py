from flask import Blueprint

bp = Blueprint("note", __name__, static_folder='static', static_url_path='/static')

from app.note import routes