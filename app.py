from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.create_all()


@app.route("/tasklist", methods=["GET"])
def get_all_task_lists():
    from models.task_list import TaskList
    return str(TaskList.query.all())


@app.route("/tasklist", methods=["POST"])
def create_task_list():
    pass


@app.route("/tasklist/<int:id>", methods=["GET"])
def get_task_list(id):
    pass


@app.route("/tasklist/<int:id>", methods=["POST"])
def update_task_list(id):
    pass


@app.route("/tasklist/<int:id>", methods=["DELETE"])
def delete_task_list(id):
    pass


if __name__ == "__main__":
    app.run(debug=True)
