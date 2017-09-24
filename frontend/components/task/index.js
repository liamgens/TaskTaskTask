import React from 'react'
import Icon from 'react-oui-icons'
import store from 'react-easy-store'

import { updateTask, } from '../../store/api'

import TaskList from '../task_list'

export default class Task extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      isEditing: false,
      description: this.props.description,
    }

    this.finishEditingTask = this.finishEditingTask.bind(this)
    this.handleBlur = this.handleBlur.bind(this)
    this.handleFocus = this.handleFocus.bind(this)
    this.handleCheckbox = this.handleCheckbox.bind(this)
    this.handleInput = this.handleInput.bind(this)
    this.handleEnter = this.handleEnter.bind(this)
    this.handleAddSublist = this.handleAddSublist.bind(this)
  }

  finishEditingTask() {
    this.setState({ isEditing: false })
    updateTask(this.props.id, this.state.description, this.state.isCompleted)
  }

  handleBlur(event) {
    updateTask(this.props.id, this.state.description, this.state.isCompleted)
  }

  handleCheckbox(event) {
    updateTask(this.props.id, this.state.description, !this.props.isCompleted)
  }

  handleEnter(event) {
    if (this.state.description != event.key === 'Enter') this.finishEditingTask()
  }

  handleFocus(event) {
    console.log('focused')
  }

  handleInput(event) {
    this.setState({ description: event.target.value })
  }

  handleAddSublist(event) {
    console.log('adding sublist')
  }

  render() {
    return (
      <div className="component__task">
        <input type="checkbox" checked={ this.props.isCompleted || false } onChange={ this.handleCheckbox } />
        <input type="text"
               onBlur={ this.handleBlur }
               onChange={ this.handleInput }
               onFocus={ this.handleFocus }
               onKeyPress={ this.handleEnter }
               value={ this.props.description } />
        {
          this.props.sublistId ?
          <TaskList listId={ this.props.sublistId } /> : (
            <div className="add_sublist" onClick={ this.handleAddSublist }>
              <Icon name="add" description="add" style={
                { height: '1rem', width: '1rem', }
              } />
            </div>
          )
        }
      </div>
    )
  }
}
