from flask import Flask

from config import Config
from app.extensions import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates',
               static_folder='static', static_url_path='/%s' % __name__)
    app.config.from_object(config_class)
    # app.config['ENV'] = 'development'
    if not app.config.get('DEBUG'):
        app.config['DEBUG'] = True
    # Initialize Flask extensions
    db.init_app(app)

# read more about this!!!!!!!

    login_manager = LoginManager()
    login_manager.login_view = 'login.login'
    login_manager.init_app(app)   

    from .models.user import Users

    @login_manager.user_loader
    def load_user(id_user):
        return Users.query.get(id_user)


    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
