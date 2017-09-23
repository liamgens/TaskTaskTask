from app.models import TaskList
from tests import BaseTestCase


class TestUpdateTaskList(BaseTestCase):

    def test_invalid_no_id(self):
        self.client.get_received()
        self.client.emit("update_task_list", {})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"error": "Task list not found."}]
        )

    def test_valid_update_title(self):
        task_list = TaskList("Foo", "Bar")
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("update_task_list", {"id": 1, "title": "Baz"})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": "Baz", "description": "Bar"}}])

    def test_valid_update_description(self):
        task_list = TaskList("Foo", "Bar")
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("update_task_list", {"id": 1, "description": "Bat"})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": "Foo", "description": "Bat"}}])

    def test_valid_update_title_description(self):
        task_list = TaskList("Foo", "Bar")
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("update_task_list", {"id": 1, "title": "Baz", "description": "Bat"})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": "Baz", "description": "Bat"}}])
