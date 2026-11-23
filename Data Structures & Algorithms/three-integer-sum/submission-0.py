class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        resultSet = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if current == 0:
                    resultSet.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                    continue
                
                if current < 0:
                    left += 1
                    continue
                
                else:
                    right -= 1
                    continue

        result = []
        for x in resultSet:
            result.append(list(x))

        return result

