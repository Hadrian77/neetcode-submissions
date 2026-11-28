class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        dpMax = [num for num in nums]
        dpMin = [num for num in nums]
        result = float('-inf')
        
        for i in range(1,len(nums)):
            if nums[i] > 0:
                dpMax[i] = max(nums[i],nums[i] * dpMax[i-1])
                dpMin[i] = min(nums[i],nums[i] * dpMin[i-1])
            else:
                dpMin[i] = min(nums[i],nums[i] * dpMax[i-1])
                dpMax[i] = max(nums[i],nums[i] * dpMin[i-1])
            
            result = max(result,dpMax[i])

        return max(result,nums[0])

            
        