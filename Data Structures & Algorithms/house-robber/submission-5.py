class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for x in range(2,len(nums)):
            dp[x] = max(dp[x-1],nums[x]+ dp[x-2])
        
        return dp[-1]