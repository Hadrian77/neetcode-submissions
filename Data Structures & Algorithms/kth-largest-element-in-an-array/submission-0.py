class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        x = 0
        while len(nums) > k:
            heapq.heappop(nums)
            k - 1
        
        return heapq.heappop(nums)