class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0

        for i in range(32):
            x = 1 & (n >> i)
            result = result | (x << (31-i))

        return result

        

        
        