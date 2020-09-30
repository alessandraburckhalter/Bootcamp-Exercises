// take a number
const num = 4;

// find the square of that number
const square = num * num;

// log the results
console.log(square)

/////////////////////////////////////////////////////////////

// function if i do know what number is
function square(number) {
    return number * number;
}

// take a number
const num = 4;

// find the square of that number
const squareNum = square(num);

/////////////////////////////////////////////////////////////

// referenciar no module file

const math = require('./math');

// take a number
const num = 4;

// find the square of that number
const squareNum = math.square(num);

// add 8
const addedNum = math.add(squareNum, 8);

console.log(addedNum)
