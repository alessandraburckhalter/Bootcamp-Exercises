const http = require("http");


const hostname = "127.0.0.1";
const port = 3000;

// http creates the server
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain') //sending back plain text
    res.end('Hello world');
})

server.listen(port, hostname, () => { //port 3000 is usually open + my local IP address
    console.log(`Server has started at http://${hostname}:${port}/`)
});


