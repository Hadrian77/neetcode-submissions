class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = defaultdict(int)
        result = len(s1)
        l = 0

        for x in s1:
            count[x] += 1
        

        for r in range(len(s2)):

            if s2[r] in count:
                if count[s2[r]] > 0:
                    result -= 1
                count[s2[r]] -= 1
                
            
            
            while r - l + 1 > len(s1):
                if s2[l] in count:
                    if count[s2[l]] >= 0:
                        result += 1
                    count[s2[l]] += 1
                l += 1

            if result == 0:
                return True;

        return False
            