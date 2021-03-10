from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')  # 이름, 모듈명, URL 프리픽스 -> 접두어 URL 설정


@bp.route('/hello')
def hello_cnc():
    return 'Hello, C&C!'


@bp.route('/')
def index():
    return 'C&C index'
