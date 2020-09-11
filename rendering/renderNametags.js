
function renderNametags(nametags) {

    let htmlString = '';

    for (let index = 0; index < nametags.length; index++) {
        const nametag = nametags[index];
        htmlString += `
            <div style="
            background-color: blue;
            color: white;
            width: 180px;
            justify-content: center;
            border: 3px solid black;
            padding: 5px;
            
            height: 40px;">Hello, my name is:</div>

            <div style="
            width: 180px;
            height: 100px;
            align-content: center;
            padding: 30px;
            margin-bottom: 10px;
            border: 3px solid black;
            ">${nametags[index]}</div> `
        
    }
    return `
        <div class="text-center mt-5">
            ${htmlString}
        </div>
    `
}

function nametags() {
    var content = document.getElementById('content');

    var nametagsAbstraction = [
       "Kamilah",
       "Kim",
       "Stuart",
       "Ron",
       "Krissy"
    ]

    content.innerHTML = renderNametags(nametagsAbstraction);

}