from flask import Blueprint, jsonify, request, abort
from flask_json import FlaskJSON, JsonError, json_response, as_json

from ..scrap.date_count import return_json
from ..scrap.languages import lang_json

# 데이터베이스 모델
from cnc.models import Commits

bp = Blueprint('main', __name__, url_prefix='/')  # 이름, 모듈명, URL 프리픽스 -> 접두어 URL 설정


@bp.route('/hello')
def hello_cnc():
    return 'Hello, C&C!'


@bp.route('/')
def index():
    return 'C&C index'


@bp.route('/compare-commits')
def compare_commits():
    StartDate = request.args.get('StartDate')
    EndDate = request.args.get('EndDate')
    MyName = request.args.get('MyName')
    OtherName = request.args.get('OtherName')

    my_data = return_json(MyName, StartDate, EndDate)
    other_data = return_json(OtherName, StartDate, EndDate)

    # 사용자 조회 실패시
    if len(my_data["count"]) == 0 or len(other_data["count"]) == 0:
        # abort(400, description="사용자 조회 실패")  # result code : 400(Bad Request)
        return json_response(isSuccess=False, code=400, message="User not found")

    return json_response(isSuccess=True, code=200, message="OK", my_data=my_data, other_data=other_data)


@bp.route('/top-five-languages')
def top_five_languages():
    MyName = request.args.get('MyName')

    top_five_languages = lang_json(MyName)

    # 사용자 조회 실패시
    if len(top_five_languages["lang"]) == 0:
        return json_response(isSuccess=False, code=400, message="User not found")

    if len(top_five_languages['lang']) < 5:
        top_five_langs = top_five_languages['lang']
        top_five_pct = top_five_languages['pct']
        return json_response(isSuccess=True, code=204, message="Not Enough Resource", top_five_langs=top_five_langs, top_five_pct=top_five_pct)

    top_five_langs = top_five_languages['lang'][:5]
    top_five_pct = top_five_languages['pct'][:5]
    return json_response(isSuccess=True, code=200, message="OK", top_five_langs=top_five_langs, top_five_pct=top_five_pct)


@bp.route('/compare-languages')
def compare_languages():
    MyName = request.args.get('MyName')
    OtherName = request.args.get('OtherName')

    my_data = lang_json(MyName)
    other_data = lang_json(OtherName)

    # 사용자 조회 실패시
    if len(my_data["lang"]) == 0 or len(other_data["lang"]) == 0:
        return json_response(isSuccess=False, code=400, message="User not found")

    no_commit_lang = []

    for lang in other_data['lang']:
        if lang not in my_data['lang']:
            no_commit_lang.append(lang)

    return json_response(isSuccess=True, code=200, message="OK", no_commit_lang=no_commit_lang)
