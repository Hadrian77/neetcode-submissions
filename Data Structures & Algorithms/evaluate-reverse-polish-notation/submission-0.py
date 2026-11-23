class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for s in tokens:
            if s == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(second + first)
            elif s == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)

            elif s == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)


            elif s == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(s))
            
        return stack.pop()