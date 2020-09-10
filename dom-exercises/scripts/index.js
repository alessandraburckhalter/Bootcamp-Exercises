

const addresses = [
    "https://google.com",
    "https://bing.com",
    "https://duckduckgo.com"
];

var aNewDiv = document.createElement('div');

for (let index = 0; index < addresses.length; index++) {
var newElement = document.createElement('a');
newElement.setAttribute('href', addresses[index]);
newElement.textContent = `Click here for ${addresses[index]}`;
aNewDiv.appendChild(newElement);
document.body.appendChild(aNewDiv);

}





