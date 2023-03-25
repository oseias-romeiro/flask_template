from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required

from db import sess
from models.User import User
from help.validators import valid_pw
from forms.LoginForm import SignInForm, SignUpForm

account_app = Blueprint("account_app", __name__)


@account_app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    form = SignInForm()
    if request.method == "GET":
        return render_template("account/sign_in.html", form=form)

    if form.validate_on_submit():

        user = sess.query(User).filter_by(
            username=form.username.data
        ).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            session['username'] = user.username
            return redirect(url_for("account_app.home"))
        else:
            flash("Incorrect username/password", "failed")
            return redirect(url_for("account_app.sign_in"))
    else:
        flash("Invalid security token", "failed")
        return redirect(url_for("account_app.sign_in"))


@account_app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()
    if request.method == "GET":
        return render_template("account/sign_up.html", form=form)

    if form.validate_on_submit():
        try:
            if form.password1.data != form.password2.data and valid_pw(form.password1.data):
                raise Exception

            user = User(
                username=form.username.data,
                password=generate_password_hash(form.password1.data)
            )
            sess.add(user)
            sess.commit()

            flash("User created", "success")

            return redirect(url_for("account_app.sign_in"))
        except:
            flash("Invalid inputs", "failed")
            return redirect(url_for("account_app.sign_up"))
    else:
        flash("Invalid security token", "failed")
        return redirect(url_for("account_app.sign_in"))


@account_app.route("/home", methods=["GET"])
@login_required
def home():
    username = session.get("username")
    return render_template("account/home.html", username=username)


@account_app.route("/logout", methods=["GET"])
@login_required
def log_out():
    logout_user()
    flash("Logging out", "success")
    return redirect(url_for("account_app.sign_in"))
