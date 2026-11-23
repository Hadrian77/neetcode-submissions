class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cache = {}
        island = 0

        for col in range(len(grid)):
            for row in range(len(grid[col])):
                if grid[col][row] == '1':
                    if not (col,row) in cache:
                        self.islandSearch(col,row,grid,cache)
                        island += 1
        

        return island    
    
    def islandSearch(self, col: int, row: int, grid, cache):

        if grid[col][row] == '0':
            return
        
        if grid[col][row] == '1':
            if (col,row) not in cache:
                cache[(col,row)] = '1'
            else:
                return

        if col - 1 >= 0:
            self.islandSearch(col - 1,row,grid,cache)
        
        if col + 1 <= len(grid) - 1:
            self.islandSearch(col + 1, row,grid,cache)

        if row - 1 >= 0:
            self.islandSearch(col,row - 1,grid,cache)

        if row + 1 <= len(grid[col]) - 1:
            self.islandSearch(col,row + 1,grid,cache)