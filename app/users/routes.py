from flask import render_template
from app.users import bp
from app.extensions import db
from app.models.user import Users
from flask_login import login_required, current_user

@bp.route('/users')
@login_required
def index():
    users = Users.query.all()
    # return render_template('users/index.html')
    return render_template('users/index.html', name = current_user.name)


# user = Users.query.all()
# print(user)
