from flask import Blueprint

# Створюємо Blueprint
bp = Blueprint('main', __name__)

# Імпортуємо роути після визначення Blueprint
from app.main import routes


