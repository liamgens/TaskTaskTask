import { socket, } from './index'

export function getTaskList(listId) {
  console.log('Getting task list ' + listId + '...')
  socket.emit('get_task_list', {
    id: listId,
  })
}