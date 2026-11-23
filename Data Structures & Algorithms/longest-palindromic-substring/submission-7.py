class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        resultlen = 0
        result = ""

        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s):
                if (r + 1) - l > 1:
                    if s[r] == s[l] and dp[l+1][r-1] == 1:
                        dp[l][r] = 1
                        if resultlen < (r + 1) - l:
                            resultlen = (r + 1) - l
                            result = s[l:r+1]
                else:
                    if s[r] == s[l]:
                        dp[l][r] = 1
                        if resultlen < (r + 1) - l:
                            resultlen = (r + 1) - l
                            result = s[l:r+1]
                l -= 1
                r += 1

            l,r = i,i+1
            
            while l >= 0 and r < len(s):
                if (r + 1) - l > 2:
                    if s[r] == s[l] and dp[l+1][r-1] == 1:
                        dp[l][r] = 1
                        if resultlen < (r + 1) - l:
                            resultlen = (r + 1) - l
                            result = s[l:r+1]
                else:
                    if s[r] == s[l]:
                        dp[l][r] = 1
                        if resultlen < (r + 1) - l:
                            resultlen = (r + 1) - l
                            result = s[l:r+1]
                l -= 1
                r += 1

        return result