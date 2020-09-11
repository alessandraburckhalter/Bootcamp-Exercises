
function renderPokerHand(pokerHand) {
    // HINT: You can use <img /> tags that point to the card images in the /cards folder
    let htmlString = ''
    for (let index = 0; index < pokerHand.length; index++) {
        const card = pokerHand[index];

        htmlString += `
            <div>
                <img width=150 src="cards/${card.value}${card.suit}.png" />
            </div>
        `    
    }
    
    return `
        <div class="text-center mt-5; d-flex flex-row justify-content-center">
            ${htmlString}
        </div>
    `
}

function pokerHand() {
    var content = document.getElementById('content');

    var pokerHandAbstraction = [
        {
            value: "K",
            suit: "C"
        },
        {
            value: "K",
            suit: "D"
        },
        {
            value: "9",
            suit: "S"
        },
        {
            value: "2",
            suit: "H"
        },
        {
            value: "9",
            suit: "H"
        }
    ];

    content.innerHTML = renderPokerHand(pokerHandAbstraction);

}