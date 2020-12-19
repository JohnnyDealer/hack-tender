import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'petya'
    DB_URI = 'postgresql+psycopg2://{user}:{password}@{url}/{db}'.format(user='postgres', password='EnterYourPasswordHere',
                                                                         url='localhost:5432  (models url, put your ulr here)', db='postgres (as an example)')
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
