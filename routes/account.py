from flask import Blueprint, render_template, request

from db import sess
from models import User

account_app = Blueprint('account_app', __name__)


@account_app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("account/sign_in.html")

    elif request.method == "POST":
        form_username = request.form.get("username")
        form_password = request.form.get("password")

        res = sess.query(User.User).filter_by(
            username=form_username,
            password=form_password
        ).first()

        if res:
            return "Success"
        else:
            return "failed"
