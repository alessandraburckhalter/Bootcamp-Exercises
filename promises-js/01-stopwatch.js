new Promise((resolve, reject) => {
    const randNum = Math.floor(Math.random() * 500);
    setTimeout(() => {
        resolve(randNum)
    }, randNum)
})