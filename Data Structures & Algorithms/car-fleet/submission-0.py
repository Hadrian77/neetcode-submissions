class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = []
        for n in range(len(position)):
            combined.append((position[n],speed[n]))
    
        combined.sort(reverse=True)
        
        result = 0
        stack = []
        for x in combined:
            position,speed = x
            time = (target - position)/speed
            if stack and stack[-1] >= time:
                continue
            else:
                result += 1
                stack.append(time)
        
        return result