from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_cnc():
        return 'Hello, C&C!'

    return app

