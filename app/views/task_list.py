from flask import jsonify

from app import socketio
from app.models import TaskList


@socketio.on("get_task_lists")
def get_all_task_lists():
    task_lists = TaskList.query.all()
    return jsonify(task_lists=[task_list.json for task_list in task_lists])


@socketio.on("create_task_list")
def create_task_list():
    pass


@socketio.on("get_task_list")
def get_task_list():
    pass


@socketio.on("update_task_list")
def update_task_list():
    pass


@socketio.on("delete_task_list")
def delete_task_list():
    pass
