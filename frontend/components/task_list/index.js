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

    const { lists, tasks, } = store.getState('lists', 'tasks')
    this.state = {
      lists: lists,
      tasks: tasks,
    }
  }

  render() {
    const { lists, tasks, } = this.state
    return (
      <div className="component__task_list">
        <div className="tasks">
        {
          lists && lists[this.props.listId] && 
          lists[this.props.listId].map((taskId, index) => (
            <Task sublistId={ tasks[taskId].sublist_id }
                  id={ tasks[taskId].id }
                  description={ tasks[taskId].description }
                  isCompleted={ tasks[taskId].is_complete }
                  listId={ tasks[taskId].list_id }
                  key={ index } />
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
