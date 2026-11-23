class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x in points:
            distance = -1 * self.distanceFromOrigin(x)
            print(distance)
            val = [distance,x[0],x[1]]
            
            if len(heap) < k:
                heapq.heappush(heap,val)
            
            elif heap[0] < val:
                heapq.heappushpop(heap,val)

        res = []
        
        for x in heap:
            res.append([x[1],x[2]])

        return res;
        


            


    def distanceFromOrigin(self,val: List):
        
        return (((0 - val[0]) ** 2) + ((0 - val[1]) ** 2) ) ** 0.5