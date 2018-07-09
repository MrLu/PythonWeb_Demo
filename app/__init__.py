# -*- coding:UTF-8 -*-
from flask import Flask
from config import *


def create_app(env=1):
    print('env:', env)
    app = Flask(__name__)  # type: Flask

    if env == 0:
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.ProductionConfig)

    print(app.config)

    from auth.auths import auths_bp
    app.register_blueprint(auths_bp)

    return app

