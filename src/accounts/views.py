from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import  current_user, login_required, logout_user

from src import db, bcrypt
from src.accounts.models import User, Boxes
from .forms import LoginForm, RegisterForm
from datetime import datetime
from ..db_operations.views import get_user_by_email, get_user_boxes, register_user, login_a_user

#blueprint for account folde
accounts_bp = Blueprint("accounts", __name__)

#register route, checks if user is already logged in, if not renders register page
@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        
        return redirect(url_for("core.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        #  automatically generates parameterized SQL queries, including escaping like ' or 1=1; -- and sanitizing input to prevent SQL injection attacks.
        register_user(form.email.data, form.password.data)
        flash("You registered and are now logged in. Welcome!", "success")

        return redirect(url_for("core.home"))

    return render_template("accounts/register.html", form=form)

#login route, checks if user is already logged in, if not redirects to login page
@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
			flash("You are already logged in.", "info")
			return redirect(url_for("core.home"))
	form = LoginForm(request.form)
	if form.validate_on_submit():
            # validate email and pass 
			user = get_user_by_email(form.email.data)
			if user and bcrypt.check_password_hash(user.password, request.form["password"]):
					login_a_user(user)
					return redirect(url_for("core.home"))
			else:
					flash("Invalid email and/or password.", "danger")
					return render_template("accounts/login.html", form=form)
	return render_template("accounts/login.html", form=form)

#logout route, redirects to home page after logout and flashes "You were logged out.
@accounts_bp.route("/logout")
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("core.home"))

#book box route, checks if user is logged in, if not redirects to login page
@accounts_bp.route("/bookings", methods=["GET"])
def bookings():
    if current_user.is_authenticated:
        user_boxes = get_user_boxes(current_user.id)
        
        return render_template("accounts/bookings.html", user_boxes=user_boxes)

    return redirect(url_for("core.home"))