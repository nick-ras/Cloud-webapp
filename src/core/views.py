from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flask import jsonify
from src import db
from src.accounts.models import Boxes
from src.accounts.forms import BookBoxForm
from datetime import datetime, timedelta

core_bp = Blueprint("core", __name__)

@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")

@core_bp.route("/locations", methods=["GET", "POST"])
@login_required
def book_box():
		form = BookBoxForm(request.form)  # Assume you have a form class for booking
		duration_opt = {6, 12, 24, 48}
		if form.validate_on_submit():
				# Get the form data
				location = form.location.data
				size = form.size.data #first one selected
				duration = form.duration.data
				print(f"location {location} size {size}")
				# Find an available box that matches the criteria
				
				box = Boxes.query.filter_by(location=location, size=size, in_use=False).with_for_update().first()
				if box:
						box.in_use = True
						#fixit: update username on box table
						box.booked_on = datetime.utcnow()
						box.user_id = current_user.id
						box.booked_until_interval15 = datetime.utcnow() + timedelta(hours=duration)
						db.session.commit()
						flash(f"you have booked {box.location} {box.size} for {duration} hours", "success")
						return redirect(url_for("core.home")) #fixit
				else:
						# Handle the case where no box is available
						db.session.rollback()
						flash("No available boxes match your criteria.", "danger")

		get_sizes= Boxes.get_available_sizes()
		return render_template("core/locations.html", form=form, get_sizes=get_sizes, duration=duration_opt)  # Assuming you have a template for booking 

@core_bp.route("/get-locations", methods=["POST"])
@login_required
def get_locations():
		sizes = request.form.get('size') #refers to the  data: { size: selectedSize  },
		print(f"sizes: {sizes} - {type(sizes)}")
		locations = Boxes.get_locations_by_size(sizes)
		print(f"locations: {locations}")
		#query is tuples, and to make it serializable i make it to a list
		location_names = [location[0] for location in locations]
		return jsonify(location_names)
