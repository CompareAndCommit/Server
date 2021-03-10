from cnc import db


class Commits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    commit_date = db.Column(db.String(20), nullable=False)


class CommitLanguages(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(30), nullable=False)  # 이름
    type = db.Column(db.String(50), nullable=False)  # 개발 분야
    count = db.Column(db.Integer, nullable=False)  # 커밋 수가 필요한가???
    language = db.Column(db.String(20), nullable=False)  # 언어
    commit_date = db.Column(db.String(20), nullable=False)  # 날짜
