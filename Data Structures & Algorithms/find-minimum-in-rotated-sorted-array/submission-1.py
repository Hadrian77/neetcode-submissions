class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        result = nums[l]

        while l <= r:
            if nums[l] <  nums[r]:
                result = min(nums[l],result)
                return result
            
            mid = (l+r) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1 
                result = min(nums[mid],result)

            else:
                r = mid - 1
                result = min(nums[mid],result)

        return result