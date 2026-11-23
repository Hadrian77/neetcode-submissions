class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def x(nums,current,arr):

            if current > len(nums) -1:
                result.append(arr)
                return

            
            arr.append(nums[current])
            x(nums,current+1,arr.copy())
            arr.pop(-1)

            
            while current + 1 < len(nums) and nums[current] == nums[current + 1]:
                current += 1

            x(nums,current+1,arr.copy())
            

        x(nums,0,[])
        return result


        