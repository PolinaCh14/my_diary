from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # app.config['ENV'] = 'development'
    if not app.config.get('DEBUG'):
        app.config['DEBUG'] = True
    # Initialize Flask extensions
    db.init_app(app)
    

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
