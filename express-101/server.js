// const http = require('http'); // core http module
// const express = require('express'); // 3rd party express module

// // getting info from the data file
// const data = require('./data');

// const hostname = '127.0.0.1'; // localhost (our computer)
// const port = 3000;

// // to start express application
// const app = express()

// const server = http.createServer(app);

// // about page
// app.get('/', (req, res) => {
//     // send back h1 for about page
//     res.send('<h1>Hello World!</h1>')
// })

// //friends list
// app.get('/friends', (req, res) => {
//     // set up empty string
//     let friends = '';
//     // loop over each item in the data
//     for (let index = 0; index < data.length; index++) {
//         const friend = data[index];
//         // append html to the friend string for each friend in the data
//         friends += `<li><a href="/friends/${friend.name}"></a></li>`
//     }
//     // send back the list of friends
//     res.send(`
//     <ul>
//         ${friends}
//     </ul>
//     `)
// })

// // friend detail page (uses route parameters indicated by :handle)
// app.get('/friends/:handle', (req, res) => {
//     // destructure the route params to get the handle from the URL
//     const { handle } = req.params;

//     // find the first friend in the data that matches the route param 'handle'
//     const friend = data.find(element => {
//         if (element.handle === handle) {
//             return true;
//         }
//         return false;
//     })

//     // if it couldn't find a friend
//     if (!friend) {
//         res
//         .status(404) // set status to 404 (not found)
//         .send(`<h1>No friend found with handle: ${handle}</h1>`)
//     // if we did find a friend
//     } else {
//     // use the details to send back a page with their info
//     res.send(`
//         <h1>${friend.name}</h1>
//         <h3>${friend.handle}</h3>
//         <p>${friend.skill}</p>
//         `)
//     }
// })

// // handle all missing pages
// app.get('*', (req, res) => {
//     res.send('<h1>Not the homepage, sorry.</h1>')
// })

// // start listening on the given port and hostname
// server.listen(port, hostname, () => {
//     // once server is listening, log to the console to say so
//     console.log(`Server running at http://${hostname}:${port}/`);
// });