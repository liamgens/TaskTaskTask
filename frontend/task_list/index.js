import React from 'react'
import PropTypes from 'prop-types'

import { lists, tasks, } from '../store'

import Task from '../task'

export default class TaskList extends React.Component {
  constructor(props) {
    super()

    this.state = {
      tasks: lists[props.listId],
    }
  }

  render() {
    console.log(this.state.tasks)
    return (
      <div className="component__task_list">
        { this.state.tasks.map((taskId, index) => <Task taskId={ taskId } key={ index } />) }
      </div>
    )
  }
}

TaskList.propTypes = {
  listId: PropTypes.number,
}
