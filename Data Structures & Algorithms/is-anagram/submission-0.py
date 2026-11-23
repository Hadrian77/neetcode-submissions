class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        cache = {}

        for letter in t:
            if letter in cache:
                cache[letter] += 1
            else:
                cache[letter] = 1
        
        for letter in s:
            if letter in cache and cache[letter] > 0:
                cache[letter] -= 1
            else:
                return False
        
        return True


       