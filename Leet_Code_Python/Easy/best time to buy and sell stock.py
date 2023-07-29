'''121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.'''

prices = [7,1,5,3,6,4]
left = 0 #Buy
right = 1 #Sell
max_profit = 0 
while right < len(prices):
    currentProfit = prices[right] - prices[left] #our current Profit
    if prices[left] < prices[right]:
        max_profit =max(currentProfit,max_profit)
    else:
        left = right
    right += 1
print(max_profit)

        







'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
#less time
for line in stdin:
    minB, profit = inf, 0
    for sell in map(int, line.rstrip()[1:-1].split(',')):
        if profit<sell-minB: profit=sell-minB
        if minB>sell: minB=sell  
    print(profit)


    '''