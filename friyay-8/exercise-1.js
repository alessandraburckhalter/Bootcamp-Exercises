function island(arr) {
    let counter = 0;

    for (let i = 0; i < arr.length; i++) {
        let firstNum = arr[i];
        let secondNum = arr[i + 1];

        if (firstNum === 1 && secondNum !== 1) {
            counter ++;
        }
        
    }
    return counter
}

let arr = [1, 0, 1, 1, 1, 0, 1, 0, 1]

console.log(island(arr))