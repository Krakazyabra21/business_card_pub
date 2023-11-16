from main import db


class HRs(db.Model):
    # if ds doesnt exist: create database.db
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    name = db.Column(db.String(50), not_null=True)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))