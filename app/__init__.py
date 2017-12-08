import os

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DATABASE_URI") is None
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite:///../database.sqlite3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

socketio = SocketIO(app)
user_count = 0


from app import events


@app.route("/")
def home():
    return render_template("home.html")
