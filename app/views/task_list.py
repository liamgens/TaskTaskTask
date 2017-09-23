from app import app
from app.models.task_list import TaskList


@app.route("/tasklist", methods=["GET"])
def get_all_task_lists():
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