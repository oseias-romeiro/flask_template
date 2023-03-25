from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import input_required


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password = PasswordField("Password", validators=[input_required()])


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password1 = PasswordField("Password", validators=[input_required()])
    password2 = PasswordField("Retype password", validators=[input_required()])

