from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user

from models.User import Role
from middleware.wraps import admin_required
from controller.account import getUsersAll, changeRole

admin_app = Blueprint("admin_app", __name__)

@admin_app.route("/panel")
@admin_required
def panel():
    others = getUsersAll()
    others = [user for user in others if user.id != current_user.id]
    return render_template("admin/panel.jinja2", users=others, roles=Role)

@admin_app.route("/panel/role", methods=["GET"])
@admin_required
def user_role():
    username = request.args.get("username")
    role = request.args.get("role")
    
    try:
        user = changeRole(username, role)
        flash(f"{user.username}'s role changed", "success")
    except:
        flash("Something went wrong", "danger")

    return redirect(url_for("admin_app.panel"))
