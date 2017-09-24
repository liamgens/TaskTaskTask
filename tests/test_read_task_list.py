from app.models import TaskList, Task
from tests import BaseTestCase


class TestReadTaskList(BaseTestCase):

    def test_read_task_list_valid_without_tasks(self):
        task_list = TaskList()
        self.db.session.add(task_list)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("read_task_list", {"id": task_list.id})
        received = self.client.get_received()

        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]["args"], [{
            "id": 1,
            "tasks": [],
        }])

    def test_read_task_list_valid_with_tasks(self):
        task_list = TaskList()
        self.db.session.add(task_list)
        self.db.session.commit()
        tasks = [
            Task(description="Foo", list_id=task_list.id),
            Task(description="Bar", list_id=task_list.id, is_complete=True),
        ]
        self.db.session.add_all(tasks)
        self.db.session.commit()

        self.client.get_received()
        self.client.emit("read_task_list", {"id": task_list.id})
        received = self.client.get_received()

        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]["args"], [{
            "id": 1,
            "tasks": [
                {
                    "id": 1,
                    "description": "Foo",
                    "is_complete": False,
                    "list_id": 1,
                    "sublist_id": None,
                },
                {
                    "id": 2,
                    "description": "Bar",
                    "is_complete": True,
                    "list_id": 1,
                    "sublist_id": None,
                },
            ],
        }])
