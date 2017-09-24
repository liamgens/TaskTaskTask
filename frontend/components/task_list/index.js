import React from 'react'
import PropTypes from 'prop-types'
import store from 'react-easy-store'

import { readTaskList, } from '../../store/api'

import Task from '../task'
import CreateNewTask from '../create_new_task'

export default class TaskList extends React.Component {
  constructor(props) {
    super(props)

    readTaskList(props.listId)
  }

  render() {
    const { lists, tasks, } = store.getState('lists', 'tasks')

    return (
      <div className="component__task_list">
        <div className="tasks">
        {
          lists && lists[this.props.listId] && 
          lists[this.props.listId].map((taskId, index) => (
            <Task taskId={ taskId } key={ index } />
          ))
        }
        </div>
        <CreateNewTask listId={ this.props.listId } />
      </div>
    )
  }
}

TaskList.propTypes = {
  listId: PropTypes.number,
}
