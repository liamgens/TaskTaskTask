from app.models import TaskList
from tests import BaseTestCase


class TestDeleteTaskList(BaseTestCase):

    def test_invalid_id_not_specified(self):
        self.client.get_received()
        self.client.emit("delete_task_list", {})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"error": "Task list not found."}])

    def test_invalid_id_does_not_exist(self):
        self.client.get_received()
        self.client.emit("delete_task_list", {"id": 1})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"error": "Task list not found."}])

    def test_valid(self):
        task_list = TaskList("Foo", "Bar")
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("delete_task_list", {"id": task_list.id})
        received = self.client.get_received()
        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"task_list": {"id": 1}}])
        self.assertIsNone(TaskList.query.filter_by(id=task_list.id).first())
