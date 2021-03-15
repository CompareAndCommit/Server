from flask import Blueprint, jsonify, request, abort
from flask_json import FlaskJSON, JsonError, json_response, as_json

from ..scrap.date_count import return_json

# 데이터베이스 모델
from cnc.models import Commits

bp = Blueprint('main', __name__, url_prefix='/')  # 이름, 모듈명, URL 프리픽스 -> 접두어 URL 설정


@bp.route('/hello')
def hello_cnc():
    return 'Hello, C&C!'


@bp.route('/')
def index():
    return 'C&C index'


@bp.route('/commits')
def commit_json():
    StartDate = request.args.get('StartDate')
    EndDate = request.args.get('EndDate')
    MyName = request.args.get('MyName')
    OtherName = request.args.get('OtherName')

    my_data = return_json(MyName, StartDate, EndDate)
    other_data = return_json(OtherName, StartDate, EndDate)

    # 사용자 조회 실패시
    if len(my_data["count"]) == 0 or len(other_data["count"]) == 0:
        abort(400, description="사용자 조회 실패")  # result code : 400(Bad Request)

    return json_response(isSuccess=True, code=200, message="OK", my_data=my_data, other_data=other_data)
