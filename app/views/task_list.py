from flask_socketio import emit

from app import socketio
from app.models import TaskList


@socketio.on("get_task_lists_request")
def get_all_task_lists():
    task_lists = TaskList.query.all()
    emit("get_task_lists_response", [task_list.json for task_list in task_lists])


@socketio.on("create_task_list_request")
def create_task_list(data):
    pass


@socketio.on("get_task_list_request")
def get_task_list(data):
    pass


@socketio.on("update_task_list_request")
def update_task_list(data):
    pass


@socketio.on("delete_task_list_request")
def delete_task_list(data):
    pass
