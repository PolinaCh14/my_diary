from flask import render_template, redirect, url_for, request, flash
from app.login import bp

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models.user import Users
from app import db
import re

@bp.route('/login')
def login():
    return render_template('login/login.html')

@bp.route('/login', methods = ['POST'])
def login_post():
    email = request.form.get('email')
    password  = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Please check your email or login')
        return redirect(url_for('login.login'))

    
    login_user(user, remember=remember)

    return redirect(url_for('users.index'))

@bp.route('/signup')
def signup():
    return render_template('login/signup.html')


def check_user_password(passwd):
    if not re.search(r"^(?=.*\d).{5,10}$",passwd):
        return False
    return True

def check_user_gmail(email):
    if not re.search(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", email):
        return False
    return True


@bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password  = request.form.get('password')
    name = request.form.get('name')
    surname = request.form.get('surname')
    birthday = request.form.get('birthday')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email = email).first()

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

    return redirect(url_for('users.index'))

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

