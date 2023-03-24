from flask import Flask, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_login import LoginManager

from routes import account
from models.User import User, Base
from db import engine, sess

app = Flask(__name__)
app.secret_key = "s3cr3t"
login_manager = LoginManager(app)

# routes projects
app.register_blueprint(account.account_app, url_prefix="/account")


@login_manager.user_loader
def load_user(user):
    return sess.query(User).filter_by(
        id=user
    ).first()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.errorhandler(401)
def custom_401(error):
    flash("Need login", "failed")
    return redirect(url_for("account_app.sign_in"))


@app.errorhandler(404)
def custom_404(error):
    return redirect(url_for("index"))


def create_admin():
    try:
        user = User(
            id=1,
            username="admin",
            password=generate_password_hash("1234")
        )
        sess.add(user)
        sess.commit()
    except:
        del user
        sess.rollback()


if __name__ == "__main__":
    # creating tables
    Base.metadata.create_all(engine)
    # insert admin user
    create_admin()

    # run flask app
    app.run()
