import React from 'react'
import Icon from 'react-oui-icons'

import CreateNewList from '../create_new_list'

const Hero = () => (
  <div className="component__hero">
      <div className="content">
        <Icon name="align-justify" description="add" fill="black" style={
          { height: '8rem', width: '8rem', }
        } />
        <h1>TaskTaskTask</h1>
        <h6>
          Collaborative task manager<br />
          with infinite possibilities.
        </h6>
        <hr />
        <div className="call-to-actions">
          <CreateNewList />
          <button className="btn"
                  onClick={ () => { location.href = location.href + '?q=1' } }>
            Open a TaskTaskTask
          </button>
        </div>
      </div>
  </div>
)

export default Hero