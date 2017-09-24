import React from 'react'

import Hero from './hero'

const Landing = () => (
  <div className="component__landing">
    <div className="container">
      <Hero />
      <div className="copy">
        <h3>Inspired by Simplicity</h3>
        <div className="row">
          <div className="six columns">
            <p>TaskTaskTask was born out of a desire to have an accessible, yet easy-to-use application to track tasks. Most general-purpose task lists don't support any nesting, but rather, maintain a simple flat structure.</p>
          </div>
        </div>

        <h3>Infinite Nesting</h3>
        <div className="row">
          <div className="six columns">
            <p>It allows you to create collaborative task lists while, supporting nesting so that you can easily keep track of your tasks, sub-tasks, sub-sub-tasks, etc. without hassle.</p>
          </div>
        </div>

        <h3>Collaborative Tasks</h3>
        <div className="row">
          <div className="six columns">
            <p>It can easily be shared among friends, family, co-workers, etc. so that everyone can see the changes as they happen.</p>
          </div>
        </div>

        <h3>Fine Grain Control</h3>
        <div className="row">
          <div className="six columns">
            <p>Share sub-lists to others and receive live updates. The limited visibility is unidirectional, so feel safe in sharing your lists.</p>
          </div>
        </div>

        <h3>Optimized for Performance</h3>
        <div className="row">
          <div className="six columns">
            <p>We use SocketIO to send data between our React clients and our Python-powered web server. We optimized our data storage and access to reduce bandwidth and increase performance.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
)

export default Landing