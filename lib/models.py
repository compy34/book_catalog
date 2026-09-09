from lib.extensions import db
from flask_login import UserMixin   


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    contacts = db.relationship('Contact', backref='owner', lazy=True)

    class Contact(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), unique = True, nullable=False)
        phone = db.Column(db.String(20), unique = True, nullable=False)
        User_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
