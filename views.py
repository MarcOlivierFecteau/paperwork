from flask import (
	Blueprint, render_template, url_for
)

views = Blueprint('views', __name__)

@views.route("/")
def home():
	return render_template("home.html")

@views.route("/about")
def about():
	return render_template("about.html")