from flask import Flask

from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #Blueprint registration
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    from .authentication import auth_login as auth_bp
    app.register_blueprint(auth_bp,url_prefix='/authentication')
    from .authentication import auth_token as token_bp
    app.register_blueprint(token_bp,url_prefix='/token')

    return app