import io from 'socket.io-client'
import store from 'react-easy-store'

import enums from './enums'

export let socket = null
export function connectSocket() {
  socket = io(location.protocol + '//' + document.domain + ':' + location.port)

  store.setState({
    lists: {},
    tasks: {},
  })

  onConnect()
  onCreateTaskList()
  onCreateTask()
  onUpdateTask()
  onReadTaskList()
}

function onConnect() {
  socket.on(enums.CONNECT, () => {
    console.log('Connected to server via socket.')
  })
}

function onCreateTaskList() {
  socket.on(enums.CREATE_TASK_LIST, data => {
    debug(enums.CREATE_TASK_LIST, [ data, ])

    const lists = store.getState('lists')
    lists[data.id] = []

    store.setState({
      lists: lists
    })
  })
}

function onCreateTask() {
  socket.on(enums.CREATE_TASK, data => {
    debug(enums.CREATE_TASK, [ data, ])

    const { lists, tasks, } = store.getState('lists', 'tasks')

    lists[data.list_id].push(data.id)
    tasks[data.id] = data

    store.setState({ lists: lists, tasks: tasks, })
  })
}

function onUpdateTask() {
  socket.on(enums.UPDATE_TASK, data => {
    debug(enums.UPDATE_TASK, [ data, ])

    const tasks = store.getState('tasks')

    tasks[data.id] = data

    store.setState({ tasks: tasks, })
  })
}

function onReadTaskList() {
  socket.on(enums.READ_TASK_LIST, data => {
    debug(enums.READ_TASK_LIST, [ data, ])

    const { lists, tasks, } = store.getState('lists', 'tasks')

    // Save tasks of the list into list store
    lists[data.id] = data.tasks.map(val => {
      return val.id
    })
    
    // Save tasks into task store
    data.tasks.forEach(elem => {
      tasks[elem.id] = elem
    })

    store.setState({ lists: lists, tasks: tasks })
  })
}

function onRemoveTask() {
  socket.on(enums.REMOVE_TASK, data => {
    debug(enums.REMOVE_TASK, [ data, ])

    const { lists, tasks, } = store.getState('lists', 'tasks')    

    store.setState({ lists: lists, tasks: tasks })
  })
}

function debug(eventName, objects) {
  console.log('===================================')
  console.log('Event: ' + eventName)
  objects.forEach(elem => console.log(elem))
}
