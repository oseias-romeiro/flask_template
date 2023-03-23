from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from db import sess
from models.User import User
from help.validators import valid_pw

account_app = Blueprint("account_app", __name__)


@account_app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("account/sign_in.html")

    elif request.method == "POST":
        form_username = request.form.get("username")
        form_password = request.form.get("password")

        res = sess.query(User).filter_by(
            username=form_username
        ).first()

        if res and check_password_hash(res.password, form_password):
            return "Success"
        else:
            return "failed"


@account_app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("account/sign_up.html")

    elif request.method == "POST":
        form_username = request.form.get("username")
        form_password1 = request.form.get("password1")
        form_password2 = request.form.get("password2")

        try:
            if form_password1 != form_password2 and valid_pw(form_password1):
                raise Exception

            user = User(
                username=form_username,
                password=generate_password_hash(form_password1)
            )
            sess.add(user)
            sess.commit()

            flash("User created", "success")

            return redirect(url_for("index"))
        except:
            flash("Invalid inputs", "failed")
            return redirect(url_for("account_app.sign_up"))

