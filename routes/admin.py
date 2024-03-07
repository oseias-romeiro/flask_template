from flask import Blueprint, render_template


from models.User import Role
from controller.wraps import admin_required
from controller.account import getUsersAll

admin_app = Blueprint("admin_app", __name__)

@admin_app.route("/panel")
@admin_required
def panel():
    return render_template("admin/panel.jinja2", users=getUsersAll(), role=Role)

