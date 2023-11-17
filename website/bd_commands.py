from . import db


class hrs(db.Model):
    # if ds doesnt exist: create database.db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))