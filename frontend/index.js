import React from 'react'
import ReactDOM from 'react-dom'
import io from 'socket.io-client'

import { getQueryParameterByName, } from './utils/query';

import CreateNewList from './components/create_new_list'
import Page from './components/page'

import './styles/index.scss'

// Obtain the listId from the query parameters.
const listId = Number(getQueryParameterByName('q')) || null

ReactDOM.render(
  <div>
    { listId ? <Page listId={ listId } /> : <CreateNewList /> }
  </div>,
  document.getElementById('app')
)