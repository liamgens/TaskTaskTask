from app.models import TaskList
from tests import BaseTestCase


class TestGetTaskList(BaseTestCase):

    def test_invalid_bad_id(self):
        self.client.get_received()
        self.client.emit("get_task_list", {"id": 1})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"error": "Task list not found."}]
        )

    def test_valid_single(self):
        task_list = TaskList("Foo", "Bar")
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("get_task_list", {"id": 1})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": "Foo", "description": "Bar"}}])

    def test_valid_multiple(self):
        task_lists = [
            TaskList("Foo", "Bar"),
            TaskList("Baz", ""),
        ]
        self.db.session.add_all(task_lists)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("get_task_list", {"id": 2})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 2, "title": "Baz", "description": ""}}])
