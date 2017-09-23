from app.models import Task
from tests import BaseTestCase


class TestDeleteTask(BaseTestCase):
    def test_delete_existing(self):

        task = Task("Angus is still a bitch", "I was just kidding", 2)

        self.db.session.add(task)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("delete_task", {"id": 1})
        received = self.client.get_received()

        received_id = received[0]["args"][0]["id"]

        self.assertIsNone(
            Task.query.filter_by(id=received_id).first()
        )

    def test_delete_non_exisiting(self):
        # assertEquals
        # received[0]["args"][0]["error"], "Task does not exist"
