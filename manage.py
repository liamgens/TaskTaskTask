from flask_script import Manager

from app import app, db, models


manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)


if __name__ == "__main__":
    db.create_all()
    manager.run()
