const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const express = require('express');
const app = express();

const server = http.createServer(app);

app.get('/', (req, res) => {
    res.send(`Hello world!`);
});

app.get('/cats', (req, res) => {
    res.send(`Meow!`)
})

app.get('/dogs', (req, res) => {
    res.send('Woof!')
})

app.get('/cats_and_dogs', (req, res) => {
    res.send('Dogs and cats living together...mass hysteria!')
})

app.get('/greet/:name', (req, res) => {
    const {name} = req.params;
    res.send(`<h1>Hello, ${name} :) </h1>`)
})

app.get('/year', (req, res) => {
    const {age} = req.query;
    const year = 2020;
    const calcAge = year - parseInt(age, 10);
    res.send(`You were born in ${calcAge}`);
})

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});