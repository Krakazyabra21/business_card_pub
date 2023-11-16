from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    # db = SQLAlchemy()
    # DB_NAME = "bd_of_bigpapa.bd"

    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
