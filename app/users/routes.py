from flask import render_template
from app.users import bp
from app.extensions import db
from app.models.user import Users

@bp.route('/')
def index():
    users = Users.query.all()
    # return render_template('users/index.html')
    return render_template('users/index.html', users=users)


# user = Users.query.all()
# print(user)
