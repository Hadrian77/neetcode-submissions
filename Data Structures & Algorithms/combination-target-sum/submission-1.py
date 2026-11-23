class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        currentList = []

        self.bk(target,currentList.copy(),result,nums,0)

        return result;

    

    def bk(self,target,currentList,result,nums,i):

        if i > len(nums) - 1:
            return

        if target == 0:
            result.append(currentList)
            return
        
        if target < 0:
            return

        
        self.bk(target,currentList.copy(),result,nums,i+1)
        currentList.append(nums[i])
        self.bk(target - nums[i],currentList.copy(),result,nums,i)

        