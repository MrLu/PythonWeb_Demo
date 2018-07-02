# -*- coding:UTF-8 -*-
from flask import Flask
from config import *


def create_app():
    app = Flask(__name__)  # type: Flask
    app.config.from_object(config.DevelopmentConfig)
    print(app.config)

    from auth.auths import auths_bp
    app.register_blueprint(auths_bp)

    return app

