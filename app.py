from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

from config import get_config

app = Flask(__name__)

# configs
config = get_config()
app.config.from_object(config)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#app.secret_key = "s3cr3t"

# extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bootstrap = Bootstrap5(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

# lazy imports
from auth.loaders import load_user
from cli_cmds import seed_cli
from controllers import account

# blueprints
app.register_blueprint(account.account_app, url_prefix="/account")

# cli
app.cli.add_command(seed_cli)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.jinja2")


@app.errorhandler(401)
def custom_401(error):
    flash("Need login", "failed")
    return redirect(url_for("account_app.sign_in"))


@app.errorhandler(404)
def custom_404(error):
    return render_template('error/404.jinja2', error=error)

