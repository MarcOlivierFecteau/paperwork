from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from paperwork.auth import login_required
from paperwork.db import get_db


forms = Blueprint("forms", __name__, url_prefix="/forms")


@forms.route("/")
def index():
    return render_template("forms/index.html")


@forms.route("/reimbursement")
def reimbursement_form():
    return render_template("reimbursement_form.html")


@forms.route("/km")
def km_form():
    return render_template("km_form.html")


@forms.route("/group-type", methods=["GET", "POST"])
def update_group_names():
    group_type = request.form.get("group_type")
    return render_template("group-name.html", group_type=group_type)


@forms.route("/submit/<form>", methods=["POST", "PUT"])
def results(form: str):
    return render_template("results.html")
