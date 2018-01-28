from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class DefaultAccessControl:
    PUBLIC_EDIT = "public-edit"  # anyone can view, check and edit
    # PUBLIC_CHECK = "public-check"  # anyone can view and check/uncheck
    # PUBLIC_CHECK_LOCAL = "public-check-local  # anyone can view and check/uncheck (locally)
    PUBLIC_VIEW = "public-view"  # anyone can view
    # TODO: password-protected variants of public controls
    PRIVATE = "private"  # only specific users can access

    @classmethod
    def readable(cls):
        return cls.writable() + [cls.PUBLIC_VIEW]

    @classmethod
    def writable(cls):
        return [cls.PUBLIC_EDIT]


class UserAccessControl:
    READ = "read"  # user can read
    # CHECK = "check"  # user can read and check
    EDIT = "edit"  # user can read, check, and edit
    MANAGE = "manage"  # user can read, check, edit, and manage (modify access)

    @classmethod
    def readable(cls):
        return cls.writable() + [cls.READ]

    @classmethod
    def writable(cls):
        return [cls.MANAGE, cls.EDIT]


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("task_list.id"), nullable=False)
    sublist_id = db.Column(db.Integer, db.ForeignKey("task_list.id"), unique=True)

    list = db.relationship("TaskList", backref=db.backref("tasks", lazy=False), foreign_keys=[list_id])
    sublist = db.relationship("TaskList", foreign_keys=[sublist_id])

    def as_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "is_complete": self.is_complete,
            "list_id": self.list_id,
            "sublist_id": self.sublist_id,
        }


class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_page_id = db.Column(db.Integer, db.ForeignKey("task_page.id"), nullable=False)

    task_page = db.relationship("TaskPage", backref=db.backref("task_lists"), foreign_keys=[task_page_id])

    def as_json(self, include_tasks=False):
        data = {"id": self.id}
        if include_tasks:
            data["tasks"] = [task.as_json() for task in self.tasks]
        return data


class TaskPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    root_task_list_id = db.Column(db.Integer, db.ForeignKey("task_list.id"), unique=True)
    default_access_control = db.Column(db.String(50), nullable=False, default=DefaultAccessControl.PUBLIC_EDIT)

    root_task_list = db.relationship("TaskList", foreign_keys=[root_task_list_id])

    def _get_user_access_level(self, user):
        access = TaskPageAccess.query.filter_by(user=user, task_page=self).first()
        if access is not None:
            return access.access_level
        return None

    def is_readable_by(self, user):
        if self.default_access_control in DefaultAccessControl.readable():
            return True
        if not user.is_authenticated:
            return False
        if self._get_user_access_level(user) in UserAccessControl.readable():
            return True
        return False

    def is_writable_by(self, user):
        if self.default_access_control in DefaultAccessControl.writable():
            return True
        if not user.is_authenticated:
            return False
        if self._get_user_access_level(user) in UserAccessControl.writable():
            return True
        return False


class TaskPageAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_page_id = db.Column(db.Integer, db.ForeignKey("task_page.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    access_level = db.Column(db.String(50), nullable=False)

    task_page = db.relationship("TaskPage")
    user = db.relationship("User")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), nullable=False, unique=True)
    _password = db.Column("password", db.String(255), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.password, value)
