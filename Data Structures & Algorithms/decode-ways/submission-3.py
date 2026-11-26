class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0 for _ in range(len(s) + 1)]
        dp[len(s)] = 1

        for i in range(len(s) -1, -1, -1):
            
            if int(s[i]) == 0:
                dp[i] = 0
                continue

            if 0 < int(s[i]) < 27  :
                dp[i] += dp[i+1]
            
            if i < len(s) - 1 and 0 < int(s[i] + s[i+1]) < 27 :
                dp[i] += dp[i+2]

            print(dp)

        return dp[0]


        