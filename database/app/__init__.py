from flask import Flask
from database.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""    Используем SQLAlchemy от Flask, потому что там синхра в комплекте    """

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
