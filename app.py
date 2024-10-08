from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

from config import get_config

BASE_ROUTE = ""
app = Flask(__name__, static_url_path=BASE_ROUTE+"/static")

# configs
config = get_config()
app.config.from_object(config)

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
from routes import account, admin, public

# blueprints
app.register_blueprint(public.public_app, url_prefix=BASE_ROUTE)
app.register_blueprint(account.account_app, url_prefix=BASE_ROUTE+"/account")
app.register_blueprint(admin.admin_app, url_prefix=BASE_ROUTE+"/admin")


# cli
app.cli.add_command(seed_cli)

# handlers

@app.errorhandler(401)
def custom_401(error):
    flash("Need login", "warning")
    return redirect(url_for("public_app.sign_in"))

@app.errorhandler(403)
def custom_403(error):
    flash("Forbidden", "warning")
    return redirect(url_for("account_app.home"))

@app.errorhandler(404)
def custom_404(error):
    return render_template('error/404.jinja2', error=error), 404

