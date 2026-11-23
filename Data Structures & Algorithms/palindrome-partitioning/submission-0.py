class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        

        def dfs(i, workinglist):

            if i == len(s):
                result.append(workinglist.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    workinglist.append(s[i : j + 1])
                    dfs(j + 1, workinglist.copy())
                    workinglist.pop()
        

        def isPalindrome(i, j):

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True


        dfs(0,[])
        return result


    
