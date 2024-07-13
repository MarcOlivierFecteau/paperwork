from flask import Blueprint, flash, render_template, redirect, request, url_for

from datetime import datetime

from scripts.generate import *

forms = Blueprint("forms", __name__, url_prefix="/forms")


@forms.route("/")
def index():
    return "<h1>This is the forms hub</h1>"


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
    results = request.form
    files = request.files
    request_pdf_filename = generate_request_pdf(results, form)
    attachments_filename = generate_attachments_pdf(files, form)
    return render_template("results.html")
