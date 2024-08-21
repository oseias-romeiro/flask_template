from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user

from forms.AuthForm import SignInForm, SignUpForm, ForgetPasswordForm
from controller.account import getUserByUsername, verifyPassword, updateLastLogin, createUser, getUserByEmail

public_app = Blueprint("public_app", __name__)

@public_app.route("/", methods=["GET"])
def index():
    return render_template("index.jinja2")

@public_app.route("/signin", methods=["GET"])
def sign_in_view():
    return render_template("sign_in.jinja2", form=SignInForm())

@public_app.route("/signin", methods=["POST"])
def sign_in():
    form = SignInForm()

    if form.validate_on_submit():
        user = getUserByUsername(form.username.data)

        if user and verifyPassword(user.password, form.password.data):
            user = updateLastLogin(user)
            login_user(user)
            return redirect(url_for("account_app.home"))
        else:
            flash("Incorrect username/password", "danger")
            return redirect(url_for("public_app.sign_in_view"))
    else:
        flash(form.errors, 'errors')
        return redirect(url_for("public_app.sign_in_view"))

@public_app.route("/signup")
def sign_up_view():
    return render_template("sign_up.jinja2", form=SignUpForm())

@public_app.route("/signup", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        try:
            createUser(form.username.data, form.email.data, form.password.data)

            flash("User created", "success")
            return redirect(url_for("public_app.sign_in"))
        except:
            flash("Username/Password already exists", 'danger')
            return redirect(url_for("public_app.sign_up"))
    else:
        flash(form.errors, 'errors')
        return redirect(url_for("public_app.sign_up"))

@public_app.route("/forgot_password", methods=["GET"])
def forgot_password_view():
    return render_template("forgot_password.jinja2", form=ForgetPasswordForm())

@public_app.route("/forgot_password", methods=["POST"])
def forgot_password():
    email = request.form.get("email")
    
    # verify email
    user = getUserByEmail(email)
    if user:
        flash("Email sent", "success")
        return redirect(url_for("public_app.sign_in"))
    else:
        flash("Email not found", "danger")
        return redirect(url_for("public_app.forget_password_view"))
