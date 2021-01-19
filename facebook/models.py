from facebook import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(6), nullable=True)
    password = db.Column(db.String(60), nullable=False)

    profile_img_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    cover_img_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    bio = db.Column(db.String(100), nullable=False, default="Add Bio")
    school = db.Column(db.String(100), nullable=False, default="Add School")
    location = db.Column(db.String(100), nullable=False, default="Add Location")
    relationship = db.Column(db.String(100), nullable=False, default="Add Relationship Status")
    posts = db.relationship('Post', backref='author', lazy=True)
    story = db.Column(db.String(20), nullable=True)
    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.email}') "


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}') "
