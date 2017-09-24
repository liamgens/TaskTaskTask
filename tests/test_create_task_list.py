from app import db
from app.models import Task, TaskList
from tests import BaseTestCase


class TestCreateTaskList(BaseTestCase):

    def test_create_task_list_valid_no_data(self):
        self.client.get_received()
        self.client.emit("create_task_list")
        received = self.client.get_received()

        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"id": 1}])

    def test_create_task_list_valid_empty_data(self):
        self.client.get_received()
        self.client.emit("create_task_list", {})
        received = self.client.get_received()

        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"id": 1}])

    def test_create_task_list_valid_with_subtask(self):
        task_list = TaskList()
        db.session.add(task_list)
        db.session.commit()
        task = Task(description="Foo Bar", list_id=task_list.id)
        db.session.add(task)
        db.session.commit()

        self.client.get_received()
        self.client.emit("create_task_list", {"task_id": task.id})
        received = self.client.get_received()

        self.assertEqual(len(received), 2)
        self.assertEqual(received[0]["name"], "create_task_list")
        self.assertEqual(received[0]["args"], [{"id": 2}])
        self.assertEqual(received[1]["name"], "update_task")
        self.assertEqual(received[1]["args"], [{
            "id": task.id,
            "description": task.description,
            "is_complete": False,
            "list_id": task.list_id,
            "sublist_id": 2,
        }])
        self.assertEqual(task.sublist_id, 2)
        self.assertEqual(TaskList.query.count(), 2)
