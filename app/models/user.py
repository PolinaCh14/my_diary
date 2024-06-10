from app.extensions import db

class Users(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(50))
    status = db.Column(db.String(15))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(60))
    birthday = db.Column(db.Date)
    date_registration = db.Column(db.Date)

    def __repr__(self):
        return f'<User "{self.id_user}">'
    
# user = Users.query.all()
# print(user)