class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cache = {}

        for x in nums:
            if x not in cache:
                cache[x] = 1
            
            else:
                cache[x] = cache[x] + 1
        
        heap = []

        for key,value in cache.items():
            heapq.heappush(heap,(-value,key))

        result = []

        for x in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

