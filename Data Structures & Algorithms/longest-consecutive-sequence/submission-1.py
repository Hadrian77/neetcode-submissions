class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numset = set(nums)
        result = 0

        for x in numset:
            if x - 1 not in numset:
                currentResult = 1
                nextNum = x + 1
                while nextNum in numset:
                    currentResult += 1
                    nextNum += 1
                
                result = max(currentResult,result)

        return result
        