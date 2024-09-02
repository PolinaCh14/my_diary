from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Optional

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[Optional(), Email()])
    name = StringField('First Name', validators=[Optional()])
    surname = StringField('Surname', validators=[Optional()])
    birthday = DateField('Date of bith', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Update')
    