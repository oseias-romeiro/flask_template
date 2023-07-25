from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import input_required, Email, EqualTo, Regexp


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password = PasswordField("Password", validators=[input_required()])


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[Email('digit a valid email address')])
    password = PasswordField("Password", validators=[
        input_required(),
        EqualTo('confirm', 'Passwords must match'),
        Regexp(
            regex='^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8,}$',
            message='Password must contain at least 8 characteres and one digit, one uppercase letter ad one special symbol'
        )
    ])
    confirm = PasswordField("Retype password")

