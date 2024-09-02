from app.extensions import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask import flash

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
    
    @staticmethod
    def get_by_email(email):
        user = Users.query.filter_by(email = email).first()
        return user
    
    def update(self, 
               email=None, 
               name=None, 
               surname=None, 
               birthday=None):
        if email:
            existing_user = Users.query.filter_by(email=email).first()
            if existing_user and existing_user.id_user != self.id_user:
                raise ValueError("Email address already exists.")
            self.email = email
        if name:
            self.name = name
        if surname:
            self.surname = surname
        if birthday:
            self.birthday = birthday
        db.session.commit()