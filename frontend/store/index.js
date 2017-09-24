import io from 'socket.io-client'
import store from 'react-easy-store'

import enums from './enums'

export let socket = null
export function connectSocket() {
  socket = io('http://' + document.domain + ':' + location.port)

  store.setState({
    lists: {},
    tasks: {},
  })

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

    const { lists } = store.getState('lists')
    lists[data.id] = []

    store.setState({
      lists: lists
    })
  })
}

function onReadTaskList() {
  socket.on(enums.READ_TASK_LIST, data => {
    debug(enums.READ_TASK_LIST, [ data, ])

    const { lists } = store.getState('lists')
    lists[data.id] = data.tasks

    store.setState({
      lists: lists
    })
  })
}

function debug(eventName, objects) {
  console.log('===================================')
  console.log('Event: ' + eventName)
  objects.forEach(elem => console.log(elem))
}
