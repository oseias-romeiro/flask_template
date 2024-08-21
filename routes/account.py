from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import logout_user, current_user

from models.User import Role
from forms.AuthForm import EditUserForm, ChangePasswordForm
from controller.account import verifyPassword, deleteUser, editUser, changePassword
from middleware.wraps import login_required

account_app = Blueprint("account_app", __name__)

@account_app.route("/home", methods=["GET"])
@login_required
def home():
    return render_template("account/home.jinja2", current_user=current_user, role=Role)

@account_app.route("/<username>/delete")
@login_required
def delete_user_view(username):
    return render_template("account/delete.jinja2", username=username)

@account_app.route("/<username>/delete", methods=["POST"])
@login_required
def delete_user(username):
    if current_user.username == username or current_user.role == Role.ADMIN:
        deleteUser(username)
        flash("User deleted", "success")
    else:
        flash("Unauthorized", "danger")
    return redirect(url_for("account_app.home"))

@account_app.route("/profile", methods=["GET"])
@login_required
def profile_view():
    form = EditUserForm()
    form.id.data = current_user.id
    form.username.data = current_user.username
    form.email.data = current_user.email

    return render_template("account/profile.jinja2", form=form)

@account_app.route("/profile", methods=["POST"])
@login_required
def profile():
    form = EditUserForm()

    if form.validate_on_submit():
        try:
            if current_user.id != int(form.id.data): raise Exception("Unauthorized")

            editUser(form.id.data, form.username.data, form.email.data, form.password.data)

            flash("User edited", "success")
            return redirect(url_for("account_app.home"))
        except:
            flash("Invalid inputs", "danger")
            return redirect(url_for("account_app.profile_view"))
    else:
        flash(list(form.errors.items())[0][1][0], 'danger')
        return redirect(url_for("account_app.profile_view"))
    
@account_app.route("/change_password", methods=["GET"])
@login_required
def change_password_view():
    form = ChangePasswordForm()
    return render_template("account/change_password.jinja2", form=form)

@account_app.route("/change_password", methods=["POST"])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        if verifyPassword(current_user.password, form.old_password.data):
            changePassword(current_user.id, form.new_password.data)
            flash("Password changed", "success")
            return redirect(url_for("account_app.home"))
        else:
            flash("Invalid inputs", "danger")
            return redirect(url_for("account_app.change_password_view"))
    else:
        flash(list(form.errors.items())[0][1][0], 'danger')
        return redirect(url_for("account_app.change_password_view"))

@account_app.route("/signout", methods=["GET"])
@login_required
def log_out():
    logout_user()
    flash("Logging out", "success")
    return redirect(url_for("public_app.sign_in"))
