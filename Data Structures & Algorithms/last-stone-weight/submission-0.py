class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        x = 0
        while x < len(stones):
            stones[x] = -1 * stones[x]
            x += 1

        heapq.heapify(stones)


        while len(stones) > 1:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1

            if  first == second:
                continue
            else:
                heapq.heappush(stones,(first - second)* -1)
        
        if stones:
            return stones[0] * -1
        else:
            return 0 
        