from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user

from app import db, bcrypt
from models.User import User
from forms.LoginForm import SignInForm, SignUpForm

account_app = Blueprint("account_app", __name__)

@account_app.route("/sign_in", methods=["GET"])
def sign_in_view():
    form = SignInForm()
    return render_template("account/sign_in.jinja2", form=form)

@account_app.route("/sign_in", methods=["POST"])
def sign_in():
    form = SignInForm()

    if form.validate_on_submit():
        user = db.session.query(User).filter_by(
            username=form.username.data
        ).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("account_app.home"))
        else:
            flash("Incorrect username/password", "danger")
            return redirect(url_for("account_app.sign_in_view"))
    else:
        flash(list(form.errors.items())[0][1][0], 'danger')
        return redirect(url_for("account_app.sign_in_view"))

@account_app.route("/sign_up", methods=["GET"])
def sign_up_view():
    form = SignUpForm()
    return render_template("account/sign_up.jinja2", form=form)

@account_app.route("/sign_up", methods=["POST"])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=bcrypt.generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.sess.commit()

            flash("User created", "success")
            return redirect(url_for("account_app.sign_in"))
        except:
            flash("Invalid inputs", "danger")
            return redirect(url_for("account_app.sign_up_view"))
    else:
        flash(list(form.errors.items())[0][1][0], 'danger')
        return redirect(url_for("account_app.sign_up_view"))

@account_app.route("/home", methods=["GET"])
@login_required
def home():
    del_user = request.args.get("del")

    if del_user:
        user = db.session.query(User).filter_by(id=del_user).first()
        db.session.delete(user)
        db.session.commit()

    users = db.session.query(User).limit(10).all()

    return render_template("account/home.jinja2", current_user=current_user, users=users)

@account_app.route("/profile", methods=["GET"])
@login_required
def profile_view():
    form = SignUpForm()
    form.username.data = current_user.username
    form.email.data = current_user.email

    return render_template("account/profile.jinja2", form=form)

@account_app.route("/profile", methods=["POST"])
@login_required
def profile():
    form = SignUpForm()

    if form.validate_on_submit():
        try:
            user = db.session.query(User).filter_by(id=current_user.id).first()
            user.username = form.username.data
            user.email = form.email.data
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()

            flash("User edited", "success")
            return redirect(url_for("account_app.home"))
        except:
            flash("Invalid inputs", "danger")
            return redirect(url_for("account_app.profile_view"))
    else:
        flash(list(form.errors.items())[0][1][0], 'danger')
        return redirect(url_for("account_app.profile_view"))

@account_app.route("/logout", methods=["GET"])
@login_required
def log_out():
    logout_user()
    flash("Logging out", "success")
    return redirect(url_for("account_app.sign_in"))
