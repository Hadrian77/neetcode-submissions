class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        self.go(nums,0,result)
        return result
        
    def go(self,nums,current,result):

        save = list(result)

        for lis in save:
            result.append(lis + [nums[current]])
        
        current += 1
        
        if current < len(nums):
            self.go(nums,current,result)


