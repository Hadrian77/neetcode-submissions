class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxheap = []
        result = []
        l = 0
        
        for r in range(len(nums)):
            heapq.heappush(maxheap,(-nums[r],r))
            print(l)

            if r - l + 1 == k:

                while maxheap[0][1] < l:
                    heapq.heappop(maxheap)
                
                result.append(-maxheap[0][0])
                l += 1
                
        return result   
    


            