from app import db
from tests import BaseTestCase
from app.models import Task, TaskList


class TestRemoveTask(BaseTestCase):
    def test_task_id_int(self):
        data = {"id": "1"}
        self.client.get_received()
        self.client.emit("remove_task", data)
        received = self.client.get_received()
        self.assertEqual(
            received[0]["args"][0]["error"], "remove_task with invalid task_id"
        )

    def test_task_id_invalid(self):
        data = {"id": 3}
        self.client.get_received()
        self.client.emit("remove_task", data)
        received = self.client.get_received()
        self.assertEqual(
            received[0]["args"][0]["error"], "remove_task with task_id of non-existent object"
        )

    def test_remove_task_wo_sublist(self):
        task = Task(description="test", list_id=2)

        self.db.session.add(task)
        self.db.session.commit()

        self.assertIsNotNone(
            Task.query.filter_by(id=task.id).first()
        )

        data = task.as_json()
        self.client.get_received()
        self.client.emit("remove_task", data)
        received = self.client.get_received()
        received_id = received[0]["args"][0]["id"]
        self.assertIsNone(
            Task.query.filter_by(id=received_id).first()
        )

    def test_remove_task_with_sublist(self):
        mainlist = TaskList()
        sublist = TaskList()
        self.db.session.add(mainlist)
        self.db.session.add(sublist)
        self.db.session.commit()

        task = Task(description="mainlisttask", list_id=1, sublist_id=2)
        task1 = Task(description="sublisttask", list_id=2)

        self.db.session.add(task)
        self.db.session.add(task1)
        self.db.session.commit()

        self.assertIsNotNone(
            Task.query.filter_by(id=1).first()
        )

        self.assertIsNotNone(
            Task.query.filter_by(id=2).first()
        )
        data = task.as_json()
        self.client.get_received()
        self.client.emit("remove_task", data)

        self.assertIsNone(
            Task.query.filter_by(id=1).first()
        )

        self.assertIsNone(
            Task.query.filter_by(id=2).first()
        )

        self.assertIsNotNone(
            TaskList.query.filter_by(id=1).first()
        )

        self.assertIsNone(
            TaskList.query.filter_by(id=2).first()
        )

    def test_remove_task_with_2sublists(self):
        mainlist = TaskList()
        sublist = TaskList()
        subsublist = TaskList()
        self.db.session.add(mainlist)
        self.db.session.add(sublist)
        self.db.session.add(subsublist)
        self.db.session.commit()
        task = Task(description="mainlisttask", list_id=1, sublist_id=2)
        task1 = Task(description="sublisttask", list_id=2, sublist_id=3)
        task2 = Task(description="subsublisttask", list_id=3)
        self.db.session.add(task)
        self.db.session.add(task1)
        self.db.session.add(task2)
        self.db.session.commit()

        self.assertIsNotNone(
            Task.query.filter_by(id=1).first()
        )

        self.assertIsNotNone(
            Task.query.filter_by(id=2).first()
        )

        self.assertIsNotNone(
            Task.query.filter_by(id=3).first()
        )

        data = task.as_json()
        self.client.get_received()
        self.client.emit("remove_task", data)

        self.assertIsNone(
            Task.query.filter_by(id=1).first()
        )

        self.assertIsNone(
            Task.query.filter_by(id=2).first()
        )

        self.assertIsNone(
            Task.query.filter_by(id=3).first()
        )

        self.assertIsNotNone(
            TaskList.query.filter_by(id=1).first()
        )

        self.assertIsNone(
            TaskList.query.filter_by(id=2).first()
        )

        self.assertIsNone(
            TaskList.query.filter_by(id=3).first()
        )
