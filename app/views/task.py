from flask import jsonify
from app import socketio
from app.models import Task
import json


@socketio.on("create_task")
def create_task(data):
    title = data.get("title")
    description = data.get("description", "")
    task_list_id = data.get("task_list_id")
    if title is None:
        emit("create_task", {"error": "Tasks must have a title."})
    elif task_list_id is None:
        emit("create_task", {"error": "Tasks must have a parent Task List."})
    else:
        new_task = Task(data.title, data.description, data.task_list_id)
        db.session.add(new_task)
        db.session.commit()
        emit("create_task", new_task.as_json, broadcast=True)


@socketio.on("update_task")
def update_task(data):
    task = Task.query.filter_by(id=data["id"]).first()
    if task is None:
        emit("update_task", {"error": "Task does not exit."})
    else:
        reponse = data
        for attribute, value in data.items():
            if attribute != "id":
                task[attribute] = value
                response[attribute] = value
        db.session.commit()
        emit("update_task", response, broadcast=True)


@socketio.on("delete_task")
def delete_task(data):
    old_task = Task.query.filter_by(id=data["id"]).first()
    if task is None:
        emit("delete_task", {"error": "Task does not exit."})
    else:
        db.session.delete(old_task)
        db.session.commit()
        data = dict(
            id=data["id"]
        )
        emit("delete_task", data, broadcast=True)
