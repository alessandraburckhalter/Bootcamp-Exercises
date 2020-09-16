const doggo = document.getElementById("doggo");

doggo.addEventListener("click", function() {
    generating()
    fetch('https://dog.ceo/api/breeds/image/random')
    .then(function(response) { return response.json();
    })
    .then(function(data) {
    const img = document.createElement('img');
    img.setAttribute('src', data.message);
    document.body.appendChild(img)
    

    const title = document.createElement('h1');
    title.textContent = data.status
    document.body.appendChild(title)

    generatingBack()
  });
})

function generating() {
    doggo.textContent = "Generating Doggo..."
}

function generatingBack() {
    doggo.textContent = "Generate Doggo"
}


const doggoSelect = document.getElementById("doggo-menu");
fetch('https://dog.ceo/api/breeds/list ').then((response) => {
    return response.json();
})
.then(function(data) {
        const breeds = data.message;
        const select = document.getElementById('dog-select');
        breeds.forEach((breed) => {
        console.log(breed);
        const option = document.createElement('option');
        option.value = breed;
        option.textContent = breed;
        select.appendChild(option);
    });
});

const select = document.querySelector('select') 
select.addEventListener('change', function() {
    fetch(` https://dog.ceo/api/breed/${this.value}/images/random`).then((response) => {
    return response.json();
})
.then(function(data) {
    const img = document.createElement('img');
    img.setAttribute('src', data.message);
    document.body.appendChild(img);
});
});