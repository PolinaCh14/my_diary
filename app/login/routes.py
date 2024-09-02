from flask import render_template, redirect, url_for, request, flash
from app.login import bp

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.user import Users
from app import db
from app.services import check_user_gmail, check_user_password

@bp.route('/login')
def login():
    return render_template('login/login.html')

@bp.route('/login', methods = ['POST'])
def login_post():
    email = request.form.get('email')
    password  = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.get_by_email(email)
    
    if not user or not check_password_hash(user.password, password):
        flash('Please check your email or login')
        return redirect(url_for('login.login'))

    
    login_user(user, remember=remember)

    return redirect(url_for('note.notes'))

@bp.route('/signup')
def signup():
    return render_template('login/signup.html')


@bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password  = request.form.get('password')
    name = request.form.get('name')
    surname = request.form.get('surname')
    birthday = request.form.get('birthday')
    remember = True if request.form.get('remember') else False

    user = Users.get_by_email(email)

    if user:
        flash('Email address already exists.')
        return redirect(url_for('login.signup'))
    elif  not check_user_password(password):
        flash("Your password must has more than 5 and less than 10 character")
        return redirect(url_for('login.signup'))
    elif not email or not password or not birthday:
        flash("The some important parameters like email, password, name and birthday can't be empty")
        return redirect(url_for('login.signup'))
    elif not check_user_gmail(email):
        flash("Unfortunately, but your email isn't valid. Try again")
        return redirect(url_for('login.signup'))
    
    new_user = Users(email=email, name=name, password=generate_password_hash(password),
                    surname = surname, birthday = birthday)

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=remember)

    return redirect(url_for('note.notes'))

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

