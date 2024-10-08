from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField
from wtforms.validators import input_required, email, equal_to, regexp


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password = PasswordField("Password", validators=[input_required()])


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[email('Digit a valid email address')])
    password = PasswordField("Password", validators=[
        input_required(),
        equal_to('confirm', 'Passwords must match'),
        regexp(
            regex='^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8,}$',
            message='Password must contain at least 8 characteres and one digit, one uppercase letter ad one special symbol'
        )
    ])
    confirm = PasswordField("Retype")

class EditUserForm(FlaskForm):
    id = HiddenField("Id")
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[email('digit a valid email address')])
    password = PasswordField("Password")


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old", validators=[input_required()])
    new_password = PasswordField("New", validators=[
        input_required(),
        equal_to('confirm', 'Passwords must match'),
        regexp(
            regex='^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8,}$',
            message='Password must contain at least 8 characteres and one digit, one uppercase letter ad one special symbol'
        )
    ])
    confirm = PasswordField("Retype")

class ForgetPasswordForm(FlaskForm):
    email = StringField("Email", validators=[input_required(), email('digit a valid email address')])
