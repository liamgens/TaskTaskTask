import io from 'socket.io-client'

import enums from './enums'

export const lists = {}
export const tasks = {}

export let socket = null
export function connectSocket() {
  socket = io('http://' + document.domain + ':' + location.port)

  onConnect()
  onCreateTaskList()
}

function onConnect() {
  socket.on(enums.CONNECT, () => {
    console.log('Connected to server via socket.')
  })
}

function onCreateTaskList() {
  socket.on(enums.CREATE_TASK_LIST, data => {
    debug(enums.CREATE_TASK_LIST, [ data, ])
    lists[data.id] = []
  })
}

function debug(eventName, objects) {
  console.log('===================================')
  console.log('Event: ' + eventName)
  objects.forEach(elem => console.log(elem))
}
