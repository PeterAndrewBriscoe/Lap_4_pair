from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'JJ'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)

    # create_database(app)

    return app

def create_database(app):
    if not path.exists('App/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')



