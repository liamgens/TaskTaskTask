import React from 'react'
import store from 'react-easy-store'

import TaskList from '../task_list'

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
        <TaskListContainer />
      </div>
    )
  }
}
