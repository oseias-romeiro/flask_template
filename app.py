from flask import Flask, render_template

from routes import account

from models.User import User, Base
from db import engine, sess

app = Flask(__name__)
app.register_blueprint(account.account_app, url_prefix="/account")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # creating tables
    Base.metadata.create_all(engine)
    # insert test user case possible
    try:
        user = User(
            id=1,
            username="user01",
            password="1234"
        )
        sess.add(user)
        sess.commit()
    except:
        del user
        sess.rollback()

    app.run()
