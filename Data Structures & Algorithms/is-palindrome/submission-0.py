class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = s.replace(' ','')

        L = 0
        R = len(string) -1

        while L < R:


            if not string[L].isalnum():
                L += 1
                continue
            
            if not string[R].isalnum():
                R -= 1
                continue

            if string[L].lower() == string[R].lower():
                L += 1
                R -= 1
                continue
            else:
                return False

        return True


