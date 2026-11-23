class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        result = 0

        for origin,height in enumerate(heights):
            lower = False
            while stack and stack[-1][1] > height:
                lower = True
                pastOrigin,pastHeight = stack.pop()
                result = max(result,((origin - pastOrigin) * pastHeight))
            
            if lower:
                stack.append((pastOrigin,height))
            else:
                stack.append((origin,height))
        
        while stack:
            origin,height = stack.pop()
            result = max(result,((len(heights)- origin) * height))
        
        return result