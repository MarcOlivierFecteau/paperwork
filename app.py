from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "penis"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_NAME}'
    db.init_app(app)

    import paperwork.views as views, paperwork.forms as forms, paperwork.auth as auth
    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth)
    app.register_blueprint(forms.forms)

    from paperwork.models import User
    with app.app_context():
        db.create_all()
        print("Created database.")
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, use_reloader=False, port=8080)