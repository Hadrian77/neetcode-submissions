class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dfs(x,y):

            if (x,y) in memo:
                return memo[(x,y)]

            if x > m - 1:
                return 0
            
            if y > n-1:
                return 0
            
            if (x,y) == (m - 1, n -1):
                return 1

            memo[(x,y)] = dfs(x,y+1) + dfs(x + 1,y)

            return memo[(x,y)]
        
        return dfs(0,0)
