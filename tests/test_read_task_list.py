from app import db
from app.models import TaskList
from tests import BaseTestCase


class TestReadTaskList(BaseTestCase):

    def test_read_task_list_valid(self):
        task_list = TaskList()
        db.session.add(task_list)
        db.session.commit()

        self.client.get_received()
        self.client.emit("read_task_list", {"id": task_list.id})
        received = self.client.get_received()

        self.assertEqual(len(received), 1)
        self.assertEqual(
            received[0]["args"],
            [{"id": 1}])
