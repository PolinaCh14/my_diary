from app.extensions import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.String(15), default="user")
    name = db.Column(db.String(50))
    surname = db.Column(db.String(60))
    birthday = db.Column(db.Date)
    date_registration = db.Column(db.Date, default=func.now())

    def __repr__(self):
        return f'<User "{self.id_user}">'
    
    def get_id(self):
        return self.id_user
    