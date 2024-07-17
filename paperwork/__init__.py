import os
from flask import Flask

def create_app(test_config=None) -> Flask:
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY="penis", # TODO: generate random key for deployment
		DATABASE=os.path.join(app.instance_path, "paperwork.sqlite"),
	)
	if test_config is None:
		app.config.from_pyfile("config.py", silent=True)
	else:
		app.config.from_mapping(test_config)
	
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import db
	db.init_app(app)

	from . import views
	app.register_blueprint(views.views)

	from . import auth
	app.register_blueprint(auth.auth)

	from . import forms
	app.register_blueprint(forms.forms)
	
	@app.route("/hello") # Test route
	def hello():
		return "Hello, World!"

	return app