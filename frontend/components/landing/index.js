import React from 'react'

import Hero from './hero'

const Landing = () => (
  <div className="component__landing">
    <Hero />
    <div className="container">
      <div className="copy">
        <div className="copy-image">
          <img className="u-max-full-width" src="/static/assets/screen2.jpg" />
        </div>
        <hr />
        <div className="row">
          <div className="eight columns">
            <h3>Inspired by Simplicity</h3>
            <p>TaskTaskTask was born out of a desire to have an accessible, yet easy-to-use application to track tasks. Most general-purpose task lists don't support any nesting, but rather, maintain a simple flat structure.</p>
            <h3>Infinite Nesting</h3>
            <p>It allows you to create collaborative task lists while, supporting nesting so that you can easily keep track of your tasks, sub-tasks, sub-sub-tasks, etc. without hassle.</p>

            <h3>Collaborative Tasks</h3>
            <p>It can easily be shared among friends, family, co-workers, etc. so that everyone can see the changes as they happen. Share sub-lists to others and receive live updates. The limited visibility is unidirectional, so feel safe in sharing your lists.</p>
            <h3>Optimized for Performance</h3>
            <p>We use SocketIO to send data between our React clients and our Python-powered web server. We optimized our data storage and access to reduce bandwidth and increase performance.</p>
          </div>
        </div>
        <hr />
        <div className="copy-image">
          <img className="u-max-full-width" src="/static/assets/tech.png" />
        </div>
      </div>
    </div>
  </div>
)

export default Landing