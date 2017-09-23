from app import db


class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False, default="")

    def __init__(self, title, description=""):
        self.title = title
        self.description = description

    def as_json(self, include_tasks=False):
        data = dict(
            id=self.id,
            title=self.title,
            description=self.description,
        )
        if include_tasks:
            tasks = [task.as_json for task in self.tasks.all()]
            data["tasks"] = tasks
        return data
