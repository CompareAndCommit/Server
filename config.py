import os


BASE_DIR = os.path.dirname(__file__)  # 현재 디렉토리(C:/projects/cmdproject)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'cnc.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False