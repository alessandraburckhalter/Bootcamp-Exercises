import React, { Component } from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'
import ToDo from './components/ToDo';
import { Button, Col, Row } from 'react-bootstrap'

class App extends React.Component {
  constructor() {
    super();

    this.state = {
      todos: [
        {
          name: ''
          
        }
      ]
    }
}

onFormSubmit = (data) => {
  this.setState({
    todos: this.state.todos.concat(data)
  })
}

removeElement = (index) => {
  const filteredArray = this.state.todos.filter((_, i) => i !== index);
  this.setState({
    todos: filteredArray
  })
}

render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Todo List</h1>
        </header>
        <ToDo onFormSubmit={ this.onFormSubmit } />
        <h3>My Tasks</h3>
        <ul>
        { this.state.todos.map((todo, index) => {
            
              return (
                <li key={ index }>{ todo.name }<Button className="btn btn-secondary p-1" >Done</Button><Button className="btn btn-danger p-1" onClick={ this.removeElement.bind(this, index) }>Remove</Button></li>
              )
      
          })}
        </ul>
        <h3>Complete Tasks</h3>
        <ul>
          
        <li><Button className="btn btn-secondary p-1">Not Done</Button><Button className="btn btn-danger p-1" >Remove</Button></li>
             
        </ul>
      </div>
    );
  }
}  

export default App;
