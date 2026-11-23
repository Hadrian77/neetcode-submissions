class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1 = {}

        for num in nums:
            if dict1.get(num):
                return num

            dict1.update({num:num})