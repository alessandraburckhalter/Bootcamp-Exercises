//Write a program that prompts the user to enter a file name, and reads in the contents of the file, convert the text to all caps, and prints it out.

//Assuming the file file1.txt contains the text: "Hello, I am file 1."

const fs = require('fs')
const readline = require("readline");

// create readline interface
const rl = readline.createInterface({
  input: process.stdin, // input
  output: process.stdout, // it's like console log
});

// use rl to ask question
rl.question("Domain Name: ", function (answer) {
    readline.close(); // close/stop the input on the terminal
    const data = fs.readFileSync(answer, 'utf8')
    console.log(data)
    rl.close();
});