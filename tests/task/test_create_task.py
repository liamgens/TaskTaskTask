from app.models import Task
from tests import BaseTestCase


class TestCreateTask(BaseTestCase):

    def test_correct_structure(self):
        task = Task("Kill Angus", "ice that bitch", 1)
        task = task.as_json

        self.client.get_received()
        self.client.emit("create_task", task)
        received = self.client.get_received()

        self.assertEqual(
            received[0]["args"],
            [{
                "id": 1,
                "title": "Kill Angus",
                "description": "ice that bitch",
                "task_list_id": 1,
                "is_complete": False,
                "in_progress": False,
                "assignee": None,
                "parent_id": None,
            }]
        )

    def test_no_title(self):
        task = Task(None, "yeet", 1)
        task = task.as_json

        self.client.get_received()
        self.client.emit("create_task", task)
        received = self.client.get_received()

        received_title = received[0]["args"][0]["error"]

        self.assertEquals(
            received_title, "Tasks must have a title."
        )

    def test_no_id(self):
        task = Task("yo", "yeet", None)
        task = task.as_json

        self.client.get_received()
        self.client.emit("create_task", task)
        received = self.client.get_received()

        received_id = received[0]["args"][0]["error"]

        self.assertEquals(
            received_id, "Tasks must have a parent Task List."
        )
