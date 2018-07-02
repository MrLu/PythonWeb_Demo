# -*- coding:UTF-8 -*-
from app import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!, 你好世界'


if __name__ == '__main__':
    app.run()

