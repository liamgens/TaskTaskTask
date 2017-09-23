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
