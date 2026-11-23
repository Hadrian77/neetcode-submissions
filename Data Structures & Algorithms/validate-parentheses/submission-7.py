class Solution:
    def isValid(self, s: str) -> bool:
        #Iterate through string
        #place open bracket on the stack
        #compare next closed bracket to top of stack
        #If it matches pop the stack
        #If it doesn't return true

        stack = []

        if(len(s)%2 or len(s)==0):
            return False

        for letter in s:
            if letter in '([{':
                stack.append(letter)
            if letter in ')]}':
                if len(stack) == 0:
                    return False
                if stack[-1] == "(" and letter == ')':
                    stack.pop()
                    continue
                if stack[-1] == "{" and letter == '}':
                    stack.pop()
                    continue
                if stack[-1] == "[" and letter == ']':
                    stack.pop()
                    continue
                else:
                    return False


        return len(stack) == 0;
