from tests import BaseTestCase


class TestCreateTaskList(BaseTestCase):

    def test_invalid_no_title(self):
        self.client.get_received()
        self.client.emit("create_task_list", {})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"error": "Task lists must have a title."}]
        )

    def test_valid_title(self):
        self.client.get_received()
        self.client.emit("create_task_list", {"title": "Foo"})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": "Foo", "description": ""}}])

    def test_valid_title_description(self):
        self.client.get_received()
        self.client.emit("create_task_list", {"title": "Foo", "description": "Bar"})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1, "title": "Foo", "description": "Bar"}}])
