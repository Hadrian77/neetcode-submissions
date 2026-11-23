class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = [-1] * len(cost)

        def dfs(index,cost):

            
            if index >= len(cost):
                return 0

            if memo[index] != -1:
                return memo[index]
            memo[index] = cost[index] + min(dfs(index + 1,cost),dfs(index + 2,cost))

            return memo[index]

        return min(dfs(0,cost),dfs(1,cost))
        