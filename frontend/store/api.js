import { lists, tasks, socket, } from './index'
import enums from './enums'

export function createTaskList(taskId = null) {
  socket.emit(enums.CREATE_TASK_LIST, taskId ? {
    task_id: taskId,
  } : {}, data => {
    location.href = location.href + '?q=' + data.id
  })
}