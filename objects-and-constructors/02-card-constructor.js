function Card(point, suit) {
    this.point = point;
    this.suit = suit;
}


Card.phototype.getImageURL = function() {
    return(`images/${this.point}_of_${this.suit}.png`)
}


// Hand Constructor
function Hand() {
    this.cards = [];
}

Hand.phototype.addCard = function(newCard) {
    this.cards.push(newCard)
}

Hand.phototype.getPoints() = function() {
        points = 0
        this.cards.forEach(element => {
            if (element.face === 'ace') {
                points += 1
            } else if (element.face === 'jack' || element.face === 'queen' || element.face === 'king') {
                points += 10
            } else {
                points += element.face
            }
        });
        this.cards.forEach(element => {
            if (element.face === 'ace' && points < 12) {
                points += 10
            }
        });
        return points;
}

const myHand = new Hand();

myHand.addCard(new Card('king', 'diamonds'))
myHand.addCard(new Card('queen', 'spades'))
myHand.addCard(new Card('ace', 'hearts'))
myHand.addCard(new Card('ace', 'clubs'))

console.log(myHand.getpoints());

// Deck constructor
function Deck() {
    this.cards = []

    const suits = ['hearts', 'clubs', 'spades', 'diamonds'];
    suits.forEach(suit => {
    for(let i = 1; i <= 13; i++) {
        this.cards.push(new Card(i, suit));
       
        }
    }) 
    this.shuffle();
}



Deck.phototype.draw = function() {
    // remove and return card
    return this.cards.pop();
}

Deck.phototype.shuffle = function() {
    // shuffle the deck
    for(let i = 0; i < this.cards.lenght; i++) {
        const randIndex = Math.floor(Math.random() * i);
        const temporary = this.cards[i]
        this.cards[i] = this.cards[randIndex]
        this.cards[randIndex] = temporary;
    }
}

Deck.phototype.numCardsLeft = function() {
    // rreturn the total number of cards in the deck
    return this.cards.length;
}


const mainDeck = new Deck();
const playerHand = new Hand();
const dealerHand = new Hand();

playerHand.addCard(mainDeck.draw());
dealerHand.addCard(mainDeck.draw());
playerHand.addCard(mainDeck.draw());
dealerHand.addCard(mainDeck.draw());

console.log(`Player has ${playerHand.getPoints()}`);
console.log(`Dealer has ${dealerHand.getPoints()}`);
console.log(`There are ${mainDeck.numCardsLeft()} cards left`)
