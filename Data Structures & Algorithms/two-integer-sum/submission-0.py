class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}
        index = 0
        for i in nums:
            if target - i in numsDict:
                return [numsDict[target-i],index]

            numsDict[i] = index
            index += 1
            
