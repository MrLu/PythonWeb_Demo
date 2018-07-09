# -*- coding:UTF-8 -*-
from app import create_app
import sys

env = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
app = create_app(env=env)


@app.route('/')
def hello_world():
    return 'Hello World!, 你好世界'


if __name__ == '__main__':
    print(app.config['HOST'], app.config['PORT'])
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
