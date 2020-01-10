from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from config import config_options

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app = Flask(__name__,instance_relative_config = True)
    app.config.from_object(Config)
    
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    db.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    
    
    return app