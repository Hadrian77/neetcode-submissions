class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        final = []

        def dfs(nums,result):

            if not nums:
                nonlocal final
                final.append(result)
                return

            for x in range(len(nums)):
                current = nums.copy()
                currentResult = result.copy()
                current.pop(x)
                currentResult.append(nums[x])
                dfs(current,currentResult)

        dfs(nums,[])

        return final