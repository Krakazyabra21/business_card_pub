from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "bd_of_bigpapa.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    app.register_blueprint(views, url_prefix="/")

    from .bd_commands import hrs

    with app.app_context():
        db.create_all()
    # create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app)
        print('Created Database!')