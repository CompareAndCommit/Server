from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)  # 모듈명

    app.config.from_object(config)  # app.config 환경 변수

    # ORM
    db.init_app(app)  # 초기화
    migrate.init_app(app, db)  # 초기화

    from . import models  # 데이터베이스 모델

    # 블루프린트
    from .views import main_views

    app.register_blueprint(main_views.bp)

    return app
