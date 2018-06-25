# -*- coding:UTF-8 -*-

from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)  # type: Flask
    app.config.from_object(config_filename)
    return app