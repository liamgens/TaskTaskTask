import React from 'react'

import { lists, tasks, } from '../../store'

import TaskList from '../task_list'

export default class Page extends React.Component {
  constructor(props) {
    super(props)    
  }

  render() {
    return (
      <div className="component__page">
        <TaskList listId={ this.props.listId } />
      </div>
    )
  }
}
