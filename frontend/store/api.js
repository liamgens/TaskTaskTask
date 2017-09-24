import { lists, tasks, socket, } from './index'
import enums from './enums'

export function createTaskList(taskId = null) {
  socket.emit(enums.CREATE_TASK_LIST, taskId ? {
    task_id: taskId,
  } : {}, data => {
    if (taskId == null) location.href = location.href + '?q=' + data.id
  })
}

export function readTaskList(listId) {
  socket.emit(enums.READ_TASK_LIST, {
    id: listId,
  })
}

export function createTask(listId, description) {
  socket.emit(enums.CREATE_TASK, {
    description: description,
    list_id: listId,
  })
}

export function updateTask(taskId, description, isCompleted) {
  socket.emit(enums.UPDATE_TASK, {
    description: description,
    id: taskId,
    is_complete: isCompleted,
  })
}

export function removeTask(taskId) {
  socket.emit(enums.REMOVE_TASK, {
    id: taskId,
  })
}
