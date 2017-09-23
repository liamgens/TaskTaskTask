from app.models import TaskList
from tests import BaseTestCase


class TestCreateTaskList(BaseTestCase):

    def test_invalid_no_title(self):
        self.client.get_received()
        self.client.emit("create_task_list", {})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"error": "Task lists must have a title."}])

    def test_valid_title(self):
        title = "Foo"
        description = ""
        self.client.get_received()
        self.client.emit("create_task_list", {"title": title})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": title, "description": description}}])
        task_list = TaskList.query.filter_by(id=1).first()
        self.assertEqual(title, task_list.title)
        self.assertEqual(description, task_list.description)

    def test_valid_title_description(self):
        title = "Foo"
        description = "Bar"
        self.client.get_received()
        self.client.emit("create_task_list", {"title": title, "description": description})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": title, "description": description}}])
        task_list = TaskList.query.filter_by(id=1).first()
        self.assertEqual(title, task_list.title)
        self.assertEqual(description, task_list.description)
