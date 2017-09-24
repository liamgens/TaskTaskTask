from app import db
from tests import BaseTestCase
from app.models import Task, TaskList


class TestRemoveTask(BaseTestCase):
    def test_task_id_int(self):
        data = {"task_id": "1"}
        self.client.get_received()
        self.client.emit("remove_task", data)
        received = self.client.get_received()
        self.assertEqual(
            received[0]["args"][0]["error"], "remove_task with invalid task_id (type)"
        )

    def test_task_id_invalid(self):
        data = {"task_id": 2}
        self.client.get_received()
        self.client.emit("remove_task", data)
        received = self.client.get_received()
        self.assertEqual(
            received[0]["args"][0]["error"], "remove_task with invalid task_id"
        )

    def test_remove_task_wo_sublist(self):
        task = Task(description="test", list_id=1)
        self.db.session.add(task)
        self.db.session.commit()

        self.assertIsNotNone(
            Task.query.filter_by(id=task.id).first()
        )

        data = task.as_json()
        print (data)
        self.client.get_received()
        self.client.emit("remove_task", data)
        received = self.client.get_received()
        print(received)
        received_id = received[0]["args"][0]["id"]
        self.assertIsNone(
            Task.query.filter_by(id=received_id).first()
        )

    def test_remove_task_with_sublist(self):
        pass
