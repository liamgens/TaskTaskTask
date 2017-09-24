import React from 'react'

import { createTask, } from '../../store/api'

export default class CreateNewTask extends React.Component {
  constructor(props) {
    super(props)

    this.handleClick = this.handleClick.bind(this)
  }

  handleClick() {
    createTask(this.props.listId, 'Another One')
  }

  render() {
    return <button onClick={ this.handleClick }>Create New Task</button>
  }
}