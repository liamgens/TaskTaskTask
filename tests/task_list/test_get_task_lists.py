from app.models import TaskList
from tests import BaseTestCase


class TestGetTaskLists(BaseTestCase):

    def test_empty(self):
        self.client.get_received()
        self.client.emit("get_task_lists")
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_lists": []}])

    def test_one_item(self):
        task_list = TaskList("Foo", "Bar")
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("get_task_lists")
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_lists": [
                {"id": 1, "title": "Foo", "description": "Bar"},
            ]}]
        )

    def test_two_items(self):
        task_lists = [
            TaskList("Foo", "Bar"),
            TaskList("Baz"),
            TaskList("Bat"),
        ]
        self.db.session.add_all(task_lists)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("get_task_lists")
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_lists": [
                {"id": 1, "title": "Foo", "description": "Bar"},
                {"id": 2, "title": "Baz", "description": ""},
                {"id": 3, "title": "Bat", "description": ""},
            ]}]
        )
