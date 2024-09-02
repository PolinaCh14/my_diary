from flask import render_template
from flask import redirect, url_for, request, flash
from app.users import bp
from app.extensions import db
from app.models.user import Users
from flask_login import login_required, current_user
from .forms import UpdateUserForm

@bp.route('/users')
@login_required
def page_user():
    return render_template('users/page-user.html', current_user = current_user)

@bp.route('/users_update', methods = ['GET','POST'])
@login_required
def update_user():
    form = UpdateUserForm(obj=current_user)
    
    if form.validate_on_submit():
        try:
            current_user.update(
                email=form.email.data,
                name=form.name.data,
                surname=form.surname.data,
                birthday=form.birthday.data
            )
            return redirect(url_for('users.page_user'))
        except ValueError as e:
            flash(str(e))
            return redirect(url_for('users.update_user'))
    
    return render_template("users/edit-user.html", form=form)
