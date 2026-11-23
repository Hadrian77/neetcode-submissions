class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)
        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                tempTuple = stack.pop()
                result[tempTuple[0]] = index - tempTuple[0]

            stack.append((index,temp))


        return result


        