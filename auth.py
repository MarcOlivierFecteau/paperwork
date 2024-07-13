from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/")
def index():
    return "<h1>This is the authentication hub</h1>"


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cip = request.form.get('cip')
        password = request.form.get('password')

        user = User.query.filter_by(cip=cip).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash(f"Connecté en tant que {user.cip}", category="success")
                return redirect("views.home")
            else:
                flash("Mot de passe incorrect.", category="error")
        else:
            flash("Le CIP n'existe pas. Veuillez vous inscrire.", category="error")
            return redirect(url_for("auth.register"))

    return render_template("auth/login.html", user=current_user)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        cip = request.form.get("cip")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User(cip=cip, password=generate_password_hash(password1, method='scrypt'), firstname="", lastname="", tel="")
        if user:
            flash("Ce CIP existe déjà. Veuiller vous connecter, ou contacter l'AGEG pour signaler un vol d'identité.")
            return redirect(url_for("auth.login"))
        elif password1 != password2:
            flash("Les mots de passe ne sont pas identiques", category="error")
        else:
            db.sesssion.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Compte créé.", category="success")
            return redirect(url_for("views.home"))

        # add user to database
    return render_template("auth/register.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Déconnexion réussie.", category="success")
    return redirect(url_for("views.home"))

@auth.route("/delete-account")
@login_required
def delete_account():
    print("delete account")
    return redirect(url_for("views.home"))