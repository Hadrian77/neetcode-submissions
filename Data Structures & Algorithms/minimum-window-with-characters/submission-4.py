class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count = defaultdict(int)
        result = ""

        if len(s) < len(t):
            return result


        for x in t:
            count[x] += 1


        l = 0
        tally = len(t)
        current = ""
        maxlength = float('inf')

        for r in range(len(s)):

            current += s[r]
            
            if s[r] in count:
                if count[s[r]] > 0:
                    tally -= 1
                count[s[r]] -= 1
            
            while tally == 0:
                if maxlength > len(current):
                    result = current
                    maxlength = len(result)

                
                if s[l] in count:
                    if count[s[l]] > -1:
                        tally += 1   
                    count[s[l]] += 1
                l += 1
                current = current[1:]

                
                

        return result
