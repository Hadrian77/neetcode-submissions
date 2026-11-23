class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        cache = {}
        resultArea = 0

        for col in range(len(grid)):
            for row in range(len(grid[col])):
                if grid[col][row] == 1:
                    if  (col,row) not in cache:
                        area = self.findArea(col,row,grid,cache) 
                        if resultArea < area:
                            resultArea = area

        return resultArea
    
    def findArea(self,col,row,grid,cache):

        if (col,row) in cache or grid[col][row] == 0:
            return 0
        
        elif grid[col][row] == 1:

            cache[(col,row)] = 1
            area = 1
            
            if col + 1 <= len(grid) -1:
                area += self.findArea(col + 1,row,grid,cache)
            
            if col - 1 >= 0:
                area += self.findArea(col - 1,row,grid,cache)
            
            if row + 1 <= len(grid[col]) - 1:
                area += self.findArea(col,row + 1,grid,cache)

            if row - 1 >= 0:
                area += self.findArea(col,row -1,grid,cache)

            return area




