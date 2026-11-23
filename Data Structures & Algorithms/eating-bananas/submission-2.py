class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        current = 0

        for i in range(len(piles)):

            if piles[i] > current:
                current = piles[i]

        low = 1
        high = current
        mid = (high + low)//2
        result = current

        while low <= high:

            hours = self.test(mid,piles)

            if hours <= h:
                result = mid
                high = mid - 1
                mid = (high + low)//2
                
            if hours > h:
                low = mid + 1
                mid = (high + low)//2
        
        return result

    def test(self,test: int, piles: List[int]) -> int:

        counter = 0

        for i in range(len(piles)):
            counter += piles[i]// test

            

            if piles[i] % test != 0:
                counter += 1

            
        print(counter)
        return counter
            
            