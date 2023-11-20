from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from flask import jsonify
from src import db
from src.accounts.models import Boxes
from src.accounts.forms import BookBoxForm
from datetime import datetime, timedelta
from ..db_operations.views import find_available_box, update_box_usage, get_available_sizes, get_locations_by_size, db_rollback

core_bp = Blueprint("core", __name__)

#main page
@core_bp.route("/")
def home():
		return render_template("core/index.html")


#booking a box
@core_bp.route("/locations", methods=["GET", "POST"])
def book_box():
		if current_user.is_authenticated:
				form = BookBoxForm(request.form)  # Assume you have a form class for booking
				duration_opt = {6, 12, 24, 48}
				if form.validate_on_submit():
						# Get the form data
						location = form.location.data
						size = form.size.data #first one selected
						duration = form.duration.data
						print(f"location {location} size {size}")
						# Find an available box that matches the criteria
						
						box = find_available_box(location, size)
						if box:
								update_box_usage(box, duration, current_user.id)
								flash(f"you have booked {box.location} {box.size} for {duration} hours", "success")
								return redirect(url_for("core.home")) #fixit
						else:
								# Handle the case where no box is available
								db_rollback()
								flash("No available boxes match your criteria.", "danger")

				result= get_available_sizes()
				print("result", result)
    		# The query result will be a list of tuples, each containing one size.
    		# You might want to extract the sizes from the tuples into a simple list.
				available_sizes = [item[0] for item in result]
				return render_template("core/locations.html", form=form, get_sizes=available_sizes, duration=duration_opt)  # Assuming you have a template for booking
		return redirect(url_for("core.home"))

# helper for locations route. It gets the locations available for a given size
@core_bp.route("/get-locations", methods=["POST"])
@login_required
def get_locations():
		sizes = request.form.get('size') #refers to the  data: { size: selectedSize  },
		print(f"sizes: {sizes} - {type(sizes)}")
		locations = get_locations_by_size(sizes)
		# print(f"locations: {locations}")
		#query is tuples, and to make it serializable i make it to a list
		location_names = [loc[0] for loc in locations]
		return jsonify(location_names)
