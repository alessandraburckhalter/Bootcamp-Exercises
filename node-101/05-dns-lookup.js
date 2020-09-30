// Write a program that prompts the user for a domain name, looks up the IP address for the domain, and prints it out

const dns = require('dns')
const readline = require("readline");

// create readline interface
const rl = readline.createInterface({
  input: process.stdin, // input
  output: process.stdout, // it's like console log
});

// use rl to make questions, whatever user inputs will go to "answer"
rl.question("Domain Name: ", function (answer) {
    readline.close(); // close/stop the input on the terminal

    // use the answer to lookup hostname
    dns.lookup(answer, function (error, address) {
        if (error) {
            console.log(error.message);
            return;
        }
        console.log("IP Address: ", address);
    })
    rl.close();
});