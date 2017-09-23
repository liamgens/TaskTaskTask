import unittest

from app import app, db, socketio


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True

        self.app = app
        self.client = socketio.test_client(self.app)
        self.db = db

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
