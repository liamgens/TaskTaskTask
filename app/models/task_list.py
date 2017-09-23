from app import db


class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False, default="")

    def __init__(self, title, description=""):
        self.title = title
        self.description = description

    @property
    def as_json(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
        )
