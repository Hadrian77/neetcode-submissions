class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = buy + 1
        result = 0

        while sell < len(prices):
            current = prices[sell] - prices[buy]
            result = max(current,result)
            
            if current < 0:
                buy = sell
                sell += 1
            else:
                sell += 1

        return result