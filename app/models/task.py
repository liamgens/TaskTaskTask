from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    task_list_id = db.Column(db.Integer, db.ForeignKey("task_list.id"), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    in_progress = db.Column(db.Boolean, default=False)
    assignee = db.Column(db.String)
    parent_id = db.Column(db.Integer, db.ForeignKey("task.id"))

    task_list = db.relationship("TaskList", backref=db.backref("tasks", lazy="dynamic"))
    parent = db.relationship("Task", backref=db.backref("children", remote_side=[id]))

    def __init__(self, title, description, task_list_id):
        self.title = title
        self.description = description
        self.task_list_id = task_list_id

    @property
    def as_json(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            task_list_id=self.task_list_id,
            is_complete=self.is_complete,
            in_progress=self.in_progress,
            assignee=self.assignee,
            parent_id=self.parent_id
        )
