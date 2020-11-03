import React, { Component } from 'react'
import { Button, Col, Row } from 'react-bootstrap'
import './ToDo.css';

export default class ToDo extends Component {
    constructor(props) {
    super(props);
    
    this.state = {
        name: ''
    }
}

onSubmit = (e) => {
    e.preventDefault();
    this.props.onFormSubmit(this.state)
    this.setState({
      name: ''
    })
  }

  onNameChange = (e) => {
    this.setState({
      name: e.target.value,
    })
  }

    render() {
        return (
        <form onSubmit={ this.onSubmit }>
            <h3>Add Task</h3>
            <div className="addTask">
        <div>
            <input type="text" id="name" value={ this.state.name } onChange={ this.onNameChange } placeholder="Enter task here"></input>
          </div>
          <Button type="submit" className="btn btn-default p-1">Add</Button>
        </div>
      </form>
        )
    }
}

