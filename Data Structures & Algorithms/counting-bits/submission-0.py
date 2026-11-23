class Solution:
    def countBits(self, n: int) -> List[int]:

        ones = []
        
        for x in range(n+1):
            
            count = 0
            while x > 0:
                if x & 1:
                    count += 1
                x = x >> 1
            ones.append(count)
        
        return ones

            
