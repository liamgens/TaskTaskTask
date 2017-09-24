import React from 'react'
import store from 'react-easy-store'

import TaskList from '../task_list'

export default class Task extends React.Component {
  render() {
    return (
      <div className="component__task">
        <div className="description">{ this.props.description }</div>
        <div className="is_completed">Completed: { this.props.isCompleted ? 'Y' : 'N' }</div>
        <div className="sublist">
          { this.props.sublistId ? <TaskList listId={ this.props.sublistId } /> : '' }
        </div>
      </div>
    )
  }
}