from app import db


class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def __init__(self, title, description=None):
        self.title = title
        self.description = description
