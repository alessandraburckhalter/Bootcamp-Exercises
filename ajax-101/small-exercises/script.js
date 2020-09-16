// const request = new XMLHttpRequest();
// request.onreadystatechange = function () {
//     console.log(this);
//     if (this.readyState === 4 && this.status === 200) {
//         console.log('Just checking')
//         console.log(this.responseText);

//         const title = document.createElement('h1');
//         title.textContent = this.responseText;
//         document.body.appendChild(title);
//     }
// }
// request.open('GET', './sample.txt');
// request.send()

fetch('/small-exercises/sample.txt')
    .then(function(response) {
        return response.text();
    })
    .then(function(text) {
        const title = document.createElement('h1');
            title.textContent = text;
            document.body.appendChild(title);
    })
