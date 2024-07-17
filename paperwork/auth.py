import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
from paperwork.db import get_db


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/")
def index():
    return "<h1>You shouldn't be here. Go <a href='views.home'>home</a>.</h1>"


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cip = request.form["cip"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE cip = ?", (cip,)
        ).fetchone()

        if user is None:
            error = "CIP incorrect."
        elif not check_password_hash(user["password"], password):
            error = "Mot de passe incorrect."

        if error is None:
            session.clear()
            session["id"] = user["id"]
            return redirect(url_for("views.home"))
        
        flash(error)

    return render_template("auth/login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        cip = request.form.get("cip")
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        db = get_db()
        error = None

        if not cip:
            error = "Un CIP est requis."
        elif not password1:
            error = "Un mot de passe est requis."
        elif password1 != password2:
            error = "Les mot de passe doivent être identiques."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (cip, password) VALUES (?, ?)",
                    (cip, generate_password_hash(password1)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Le CIP {cip} est déjà enregistré."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@auth.before_app_request
def load_logged_in_user() -> None:
    user_id = session.get("id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("views.home"))


@auth.route("/delete-account")
def delete_account():
    # TODO
    flash("Cette fonctionalité n'est pas encore disponible.")
    return redirect(url_for("views.home"))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        
        return view(**kwargs)

    return wrapped_view
