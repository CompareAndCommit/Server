from flask import Flask, render_template

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)  # 모듈명

    app.config.from_object(config)  # app.config 환경 변수

    # FLASK_JSON configuration
    app.config['JSON_ADD_STATUS'] = False

    # ORM
    db.init_app(app)  # 초기화
    migrate.init_app(app, db)  # 초기화

    from . import models  # 데이터베이스 모델

    # 블루프린트
    from .views import main_views

    app.register_blueprint(main_views.bp)

    # 오류 페이지
    app.register_error_handler(404, page_not_found)

    return app
