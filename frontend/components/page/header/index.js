import React from 'react'
import Icon from 'react-oui-icons'

export default class Header extends React.Component {
  render() {
    return (
      <div className="component__header">
        <Icon name="align-justify" description="add" fill="white" style={
          { height: '3rem', width: '3rem', }
        } />
        <a href="/" className="logo">TaskTaskTask</a>
      </div>
    )
  }
}