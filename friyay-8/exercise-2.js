const stock1 = [8, 7, 1, 3, 5]

function maxProfit(prices) {
    let minPrice = prices[0];
  // minprice will start at index ($8)
    let maxProfit = prices[1] - prices[0];
  // Set maxProfit at $-1 (7-8)
    for (let i = 1; i < prices.length; i++) {
    let currentPrice = prices[i];
    // current price is $7
    let potentialProfit = currentPrice - minPrice;
    // $7 - 8 = potential profit ($-1)
    maxProfit = Math.max(maxProfit, potentialProfit);
    // Math.max finds the highest number ($-1, $-1) ---> maxProfit is now $-1
    console.log('Max Profit is ' + maxProfit)
    minPrice = Math.min(minPrice, currentPrice);
    // Math.min finds the lowest number ($8, $7) ---->minPrice is now $7
    console.log('Min Price is ' + minPrice)
}
  // Return $-1
    return maxProfit;
}
console.log('Max Profit is: ', maxProfit(stock1))

function maxProfit(arr) {
    let minPrice = Math.min(...arr)
    let maxProfit = 0;
}