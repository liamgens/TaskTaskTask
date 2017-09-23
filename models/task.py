from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    in_progress = db.Column(db.Boolean, default=False)
    assignee = db.Column(db.String)
    parent_id = db.Column(db.Integer)
    task_list_id = db.Column(db.Integer, nullable=False)



