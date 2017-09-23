from app.models import Task
from tests import BaseTestCase


class TestUpdateTask(BaseTestCase):
    def test_changes_and_exists(self):
        task = Task("Title", "Description", 1)
        self.db.session.add(task)
        self.db.session.commit()

        updated_task = {
            "id": task.id,
            "title": "Changed_title",
            "task_list_id": 2
        }

        self.client.get_received()
        self.client.emit("update_task", updated_task)
        received = self.client.get_received()
        received_id = received[0]["args"][0]["id"]
        queried_task = Task.query.filter_by(id=received_id).first()

        self.assertEqual(
            "Changed_title", getattr(queried_task, "title")
        )
        self.assertEqual(
            2, getattr(queried_task, "task_list_id")
        )

    def test_changes_and_dne(self):
        updated_task = {
            "id": 1,
            "title": "Changed_title",
            "task_list_id": 2
        }

        self.client.get_received()
        self.client.emit("update_task", updated_task)
        received = self.client.get_received()
        received_message = received[0]["args"][0]["error"]

        self.assertEqual(
            "Task does not exit.", received_message
        )
