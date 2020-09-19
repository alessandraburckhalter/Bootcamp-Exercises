function timer() {
    return new Promise((resolve, reject) => {
        const randNum = Math.floor(Math.random() * 500);
        setTimeout(() => {
            resolve(randNum)
    }, randNum)
})
}

const tortoise = timer()
const hare = timer();

Promise.all([tortoise, hare])
    .then(results => {
        const [tortoiseResult, hareResult] = results;
        // Display the winner (or determine if it's a tie)
        if (tortoiseResult > hareResult) {
            console.log('Tortoise Wins')
        } else if (hareResult > tortoiseResult) {
            console.log('Hare wins')
        } else if (hareResult === tortoiseResult) {
            console.log('DRAW')
        }
        // Display the total time it took for each animal
        console.log(`Tortoise: ${tortoiseResult}`);
        console.log(`Hare: ${hareResult}`);
    })