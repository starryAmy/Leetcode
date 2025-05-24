/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let profit = 0
  let cheapest = prices[0]
  for (i = 1; i < prices.length; i++) {
      if (prices[i] < cheapest) {
          cheapest = prices[i]
      } else {
        profit = Math.max(profit, prices[i] - cheapest);
      }
  }
  return profit
};
