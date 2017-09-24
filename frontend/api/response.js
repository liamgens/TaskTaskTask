import { socket, } from './index'

export function onConnect(cb) {
  socket.on('connect', data => cb(data))
}

export function onGetTaskList(cb) {
  socket.on('get_task_list', data => cb(data))
}