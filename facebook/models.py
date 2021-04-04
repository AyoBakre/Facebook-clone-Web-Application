from facebook import db
from datetime import datetime
from werkzeug.security import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(64), index=True, nullable=False)
    l_name = db.Column(db.String(64), index=True, nullable=False)
    dob = db.Column(db.DateTime, nullable=True, index=True)
    gender = db.Column(db.String(6), index=True, nullable=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
