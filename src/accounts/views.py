from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, login_required, logout_user
from src import db, bcrypt
from src.accounts.models import User, Boxes
from src.accounts.forms import BookBoxForm
from .forms import LoginForm, RegisterForm
from datetime import datetime

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return redirect(url_for("core.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("You registered and are now logged in. Welcome!", "success")

        return redirect(url_for("core.home"))

    return render_template("accounts/register.html", form=form)

@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
# 	tivoli_box = Boxes(size=2, location='Tivoli Gardens, Copenhagen', in_use=False, )
# 	mermaid_box = Boxes(size=1, location='The Little Mermaid, Copenhagen')
# 	nyhavn_box = Boxes(size=3, location='Nyhavn, Copenhagen')
# 	# Assuming you have a Session class ready for adding and committing
# 	db.create_all() #when making changes to the database
# 	db.session.add(tivoli_box)
# 	db.session.add(mermaid_box)
# 	db.session.add(nyhavn_box)
# 	db.session.commit()
# 	print("after box creation")
	if current_user.is_authenticated:
			flash("You are already logged in.", "info")
			return redirect(url_for("core.home"))
	form = LoginForm(request.form)
	if form.validate_on_submit():
			user = User.query.filter_by(email=form.email.data).first()
			if user and bcrypt.check_password_hash(user.password, request.form["password"]):
					login_user(user)
					return redirect(url_for("core.home"))
			else:
					flash("Invalid email and/or password.", "danger")
					return render_template("accounts/login.html", form=form)
	return render_template("accounts/login.html", form=form)


@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login"))

@accounts_bp.route("/locations", methods=["GET", "POST"])
@login_required
def book_box():
		form = BookBoxForm(request.form)  # Assume you have a form class for booking
		if form.validate_on_submit():
				# Get the form data
				selected_location = form.location.data
				selected_size = form.size.data
				selected_duration = form.duration.data

				# Find an available box that matches the criteria
				
				box = Boxes.query.filter_by(location=selected_location, size=selected_size, in_use=False).first()
				print(f"box: {box}")
				if box:
						# Update the box status and booked_on time
						box.in_use = True
						box.booked_on = datetime.utcnow()
						db.session.commit()
						# Optionally schedule a task to unbook the box later (see previous examples)
						# ...

						flash(f"You have booked a {selected_size}-sized box at {selected_location} for {selected_duration} hours.", "success")
						return redirect(url_for("core.home"))
				else:
						flash("No available boxes match your criteria.", "danger")

		selected_size = request.form.get('size')
		locations_list = Boxes.get_locations_by_size(selected_size)
		return render_template("core/locations.html", form=form, location_list=locations_list)  # Assuming you have a template for booking
