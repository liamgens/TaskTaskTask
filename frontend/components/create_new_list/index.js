import React from 'react'

import { createTaskList, } from '../../store/api'

export default class CreateNewList extends React.Component {
  render() {
    return (
      <button className="btn btn-accent"
              onClick={ () => createTaskList() }>
        Create a New List
      </button>
    )
  }
}
