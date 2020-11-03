import React, {Component} from "react";
import Button from 'react-bootstrap/Button';

class StepBtn extends Component{

    constructor(){
        super();
        this.state = {
            number: 0,
            numberBefore: 0
        };
    };

    handleChange = (event) => {
        event.preventDefault();
        let currentNumber = this.state.number;
        this.setState({number: event.target.name === "subtract" ? currentNumber - 1 : currentNumber + 1})
    }

    handleNewInput = (event) => {
        let currentNumber = this.state.number;
        
        console.log(typeof parseInt(event.target.value, 10), parseInt(event.target.value, 10))
       this.setState({number: event.target.name === 'displayNumber' && isNaN(parseInt(event.target.value, 10)) ? currentNumber : parseInt(event.target.value, 10)})  
    }
    empty = (event) => {
        this.setState({number: '', numberBefore: this.state.number})
    }

    blurredOut = (event) => {
        this.setState({ number: this.state.number === '' ? this.state.numberBefore : this.state.number});
    }


    render(){
        return(
            <form>
                <Button variant="success" size="md" name='minus' onClick={this.handleChange}>
                    -
                </Button>
                <input type='text' name="display" value={this.state.number}  onChange={this.handleNewInput} onFocus={this.empty} onBlur={this.blurredOut}/>
                <Button variant="success" size="md" name='plus' onClick={this.handleChange}>
                    +
                </Button>
            </form>
        )
    }
}

export default StepBtn;