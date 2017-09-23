from flask import jsonify
from app import socketio
from app.models import Task
import json


@socketio.on("create_task_request")
def create_task(data):
    new_task = Task(data.title, data.description, data.task_list_id)
    db.session.add(new_task)
    db.session.commit()
    emit("create_task_response", new_task.as_json, broadcast=True)


@socketio.on("update_task_request")
def update_task(data):
    task = Task.query.filter_by(id=data["id"]).first()
    reponse = data
    for attribute, value in data.items():
        if attribute != "id":
            task[attribute] = value
            response[attribute] = value
    db.session.commit()
    emit("update_task_response", response, broadcast=True)


@socketio.on("delete_task_request")
def delete_task(data):
    old_task = Task.query.filter_by(id=data["id"]).first()
    db.session.delete(old_task)
    db.session.commit()
    data = dict(
        id=data["id"]
    )
    emit("delete_task_response", data, broadcast=True)
