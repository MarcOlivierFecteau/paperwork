import pytest

from flask import g, session

from paperwork.db import get_db


def test_register(client, app):
	assert client.get("/auth/register").status_code == 200
	response = client.post(
		"/auth/register",
		data={"cip": "ageg2024", "password1": "test", "password2": "test"}
	)
	assert response.headers["Location"] == "/auth/login"

	with app.app_context():
		assert get_db().execute(
			"SELECT * FROM user WHERE cip = 'ageg2024'",
		).fetchone() is not None


@pytest.mark.parametrize(("cip", "password1", "password2", "message"), (
	("", "", "", b"Le CIP est requis."),
	("ageg2024", "", "", b"Un mot de passe est requis."),
	("ageg2024", "test", "", b"Les mot de passe ne sont pas identiques."),
	("test0042", "test", "test", f"Le CIP est déjà enregistré."),
))
def test_register_validate_input(client, cip, password1, password2, message):
	response = client.post(
		"/auth/register",
		data={"cip": cip, "password1": password1, "password2": password2}
	)
	assert message in response.data


def test_login(client, auth):
	assert client.get("/auth/login").status_code == 200
	response = auth.login()
	assert response.header["Location"] == "/"

	with client:
		client.get("/")
		assert session["id"] == 1
		assert g.user["cip"] == "test0042"


@pytest.mark.parametrize(("cip", "password", "message"), (
	("test0041", "test", b"CIP incorrect."),
	("test0042", "test1", b"Mot de passe incorrect."),
))
def test_login_validate_input(auth, cip, password, message):
	response = auth.login(cip, password)
	assert message in response.data


def test_logout(client, auth):
	auth.login()

	with client:
		auth.logout()
		assert "id" not in session