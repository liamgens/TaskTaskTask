import os

from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DATABASE_URI") is None
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "yg^OyviYV75i542@467yi;.>khIYuiO")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite:///../database.sqlite3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

Session(app)

socketio = SocketIO(app, manage_session=False)
user_count = 0

login_manager = LoginManager(app)


@login_manager.user_loader
def _load_user(user_id):
    from app.models import User
    return User.query.get(user_id)


from app import events
from app import views
