class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for x in coins:
                if x > i:
                    continue
                else:
                    if dp[i - x] != -1:
                        if dp[i] > 0:
                            dp[i] = min(1 + dp[i-x],dp[i])
                        else:
                            dp[i] = 1 + dp[i-x]
            

        return dp[amount]