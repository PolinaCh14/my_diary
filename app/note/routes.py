from flask import render_template
from app.note import bp
from app.extensions import db

from flask_login import login_required, current_user

@bp.route('/notes')
@login_required
def notes():
    return render_template('note/main-note-page.html')