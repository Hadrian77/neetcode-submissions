class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for x in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap,x)
            else:
                self.add(x)

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        
        elif self.heap[0] < val:
            heapq.heappushpop(self.heap,val)
        
        return self.heap[0]
        
