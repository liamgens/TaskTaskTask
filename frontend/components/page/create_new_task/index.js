import React from 'react'
import Icon from 'react-oui-icons'

import { createTask, } from '../../../store/api'

export default class CreateNewTask extends React.Component {
  constructor(props) {
    super(props)

    this.state = { input: '' }

    this.handleClick = this.handleClick.bind(this)
    this.handleEnter = this.handleEnter.bind(this)
    this.handleInput = this.handleInput.bind(this)

  }

  handleClick() {
    if (this.state.value && this.state.value !== '') {
      createTask(this.props.listId, this.state.value)
      this.setState({ value: '', })
    }
  }

  handleEnter(event) {
    if (event.key === 'Enter' && this.state.value !== '') this.handleClick()
  }

  handleInput(event) {
    this.setState({ value: event.target.value, })
  }

  render() {
    return (
      <div className="component__create_new_task">
        <div className="content">
          <input type="text"
                onChange={ this.handleInput }
                onKeyPress={ this.handleEnter }
                value={ this.state.value || '' } />
          <div className="add_task" onClick={ this.handleClick }>
            <Icon name="add" description="add" style={
              { height: '1rem', width: '1rem', }
            } />
          </div>
        </div>
      </div>
    )
  }
}