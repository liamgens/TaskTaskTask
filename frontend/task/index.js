import React from 'react'

import TaskList from '../task_list'

import { lists, tasks, } from '../store'

export default class Task extends React.Component {
  constructor(props) {
    super()

    this.state = tasks[props.taskId]
  }
  
  render() {
    return (
      <div className="component__task">
        <div className="description">{ this.state.description }</div>
        <div className="is_completed">Completed: { this.state.isCompleted ? 'Y' : 'N' }</div>
        <div className="sublist">
          { this.state.sublistId ? <TaskList listId={ this.state.sublistId } /> : '' }
        </div>
      </div>
    )
  }
}