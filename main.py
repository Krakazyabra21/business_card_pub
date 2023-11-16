from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import views
from os import path

db = SQLAlchemy()
DB_NAME = "bd_of_bigpapa.bd"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)
app.register_blueprint(views, url_prefix="/views")





# def create_database(apli):
#     if not path.exists(DB_NAME):
#         db.create_all(apli)


# create_database(app)


if __name__ == '__main__':
    app.run(debug=True, port= 8000)

