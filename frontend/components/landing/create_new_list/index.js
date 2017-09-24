import React from 'react'

import { createTaskList, } from '../../../store/api'

export default class CreateNewList extends React.Component {
  render() {
    return (
      <div className="component__create_new_list">
        <button className="btn btn-accent"
                onClick={ () => createTaskList() }>
          Create a New List
        </button>
      </div>
    )
  }
}
