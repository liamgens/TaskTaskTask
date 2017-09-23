from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def test():
    return "test"

@app.route("/tasklist", methods=["GET", "POST"])
def tasklist():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    


@app.route("/tasklist/<tasklist_id>", methods=["GET", "POST", "DELETE"])
def tasklist(tasklist_id):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    elif request.method == "DELETE":
        pass





if __name__ == "__main__":
    app.run(debug=True)
