from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user

from models.User import Role
from forms.AuthForm import SignInForm, SignUpForm, EditUserForm, ForgetPasswordForm, ChangePasswordForm
from controller.account import getUserByUsername, verifyPassword, updateLastLogin, createUser, deleteUser, editUser, getUserByEmail, changePassword
from controller.wraps import admin_required

account_app = Blueprint("account_app", __name__)

@account_app.route("/signin", methods=["GET"])
def sign_in_view():
    form = SignInForm()
    return render_template("account/sign_in.jinja2", form=form)

@account_app.route("/signin", methods=["POST"])
def sign_in():
    form = SignInForm()

    if form.validate_on_submit():
        user = getUserByUsername(form.username.data)

        if user and verifyPassword(user.password, form.password.data):
            user = updateLastLogin(user)
            login_user(user)
            return redirect(url_for("account_app.home"))
        else:
            flash("Incorrect username/password", "danger")
            return redirect(url_for("account_app.sign_in_view"))
    else:
        flash(list(form.errors.items())[0][1][0], 'danger')
        return redirect(url_for("account_app.sign_in_view"))

@account_app.route("/create", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()

    if request.method == "GET":
        return render_template("account/sign_up.jinja2", form=form)

    elif request.method == "POST":
        if form.validate_on_submit():
            try:
                createUser(form.username.data, form.email.data, form.password.data)

                flash("User created", "success")
                return redirect(url_for("account_app.sign_in"))
            except:
                flash("Error persisting data", "danger")
                return redirect(url_for("account_app.sign_up"))
        else:
            return render_template("account/sign_up.jinja2", form=form, errors=form.errors)

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
    if current_user.role == Role.ADMIN:
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

@account_app.route("/forgot_password", methods=["GET"])
def forgot_password_view():
    form = ForgetPasswordForm()
    return render_template("account/forgot_password.jinja2", form=form)

@account_app.route("/forgot_password", methods=["POST"])
def forgot_password():
    email = request.form.get("email")
    
    # verify email
    user = getUserByEmail(email)
    if user:
        flash("Email sent", "success")
        return redirect(url_for("account_app.sign_in"))
    else:
        flash("Email not found", "danger")
        return redirect(url_for("account_app.forget_password_view"))
    
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

@account_app.route("/logout", methods=["GET"])
@login_required
def log_out():
    logout_user()
    flash("Logging out", "success")
    return redirect(url_for("account_app.sign_in"))
