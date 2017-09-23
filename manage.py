from flask_script import Manager

from app import app, db, models, socketio


manager = Manager(app, with_default_commands=False)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)


@manager.command
def runserver():
   socketio.run(app)


if __name__ == "__main__":
    db.create_all()
    manager.run()
