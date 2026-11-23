class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        if len(prices) < 2:
            return 0

        buy = 0
        sell = buy + 1
        maxprofit = 0

        while buy < len(prices):

            profit = prices[sell] - prices[buy]
            maxprofit = max(profit,maxprofit)

            if profit < 0 or sell == len(prices) - 1:
                buy += 1
            else:
                sell += 1
        return maxprofit