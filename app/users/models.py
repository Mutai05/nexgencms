from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Explicitly set the table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
