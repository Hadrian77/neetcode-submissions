class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = -1
        fast = 0
        slow = 0
        slow2 = 0
        while True:
            

            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

            if slow == fast:
                slow2 = 0
                break;
        
        while True:
            slow2 = nums[slow2]
            slow= nums[slow]
            if slow == slow2:
                return slow





        
        
