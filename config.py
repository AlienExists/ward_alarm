import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_MIGRATE_REPO = "db"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123@localhost/project1_db'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                          'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_ADD_STATUS = False
    JSON_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'