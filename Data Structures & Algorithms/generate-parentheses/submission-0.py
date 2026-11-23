class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []


        

        def paren(openNum,closeNum):

            if openNum == closeNum == n:
                result.append("".join(stack))

            if openNum < n:
                stack.append('(')
                paren(openNum + 1,closeNum)
                stack.pop()
            
            if closeNum < openNum:
                stack.append(')')
                paren(openNum,closeNum + 1)
                stack.pop()

        paren(0,0)
        return result