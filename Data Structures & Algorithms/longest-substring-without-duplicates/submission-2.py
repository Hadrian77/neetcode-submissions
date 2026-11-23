class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        


        start = 0
        end = start
        count = 0

        while end < len(s):
            
            noDuplicate = True
            cache = {}

            while noDuplicate:
                

                if end < len(s) and s[end] not in cache:
                    cache[s[end]] = 1
                    end += 1
                else:
                    noDuplicate = False
                    count = max((end - start),count)
                    start += 1
                    end = start


        return count