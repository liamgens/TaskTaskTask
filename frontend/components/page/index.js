import React from 'react'
import store from 'react-easy-store'

import Header from './header'
import TaskList from './task_list'

const TaskListConnect = store.connect(TaskList)({
  lists: 'list',
  tasks: 'tasks',
})

export default class Page extends React.Component {
  render() {
    const TaskListContainer = TaskListConnect({
      listId: this.props.listId,
    })

    return (
      <div className="component__page">
        <Header />
        <div className="component__task_list_container">
          <TaskListContainer />
        </div>
      </div>
    )
  }
}
