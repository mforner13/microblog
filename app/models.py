from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Masterclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(400))
    timestamp = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    location = db.relationship('Location', backref='location', lazy='dynamic')

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50), index=True)
    street_number = db.Column(db.String(5)) #should keep numbers as strings unless going to do calculations?
    street_name = db.Column(db.String(100), index=True)
    town_or_city = db.Column(db.String(50), index=True)
    postcode = db.Column(db.String(9), index=True)
    masterclass_id = db.Column(db.Integer, db.ForeignKey('masterclass.id'))




