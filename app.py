# -*- coding:UTF-8 -*-

from app import create_app

app = create_app('app.config')

@app.route('/')
def hello_world():
    return 'Hello World!, 你好世界'

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
