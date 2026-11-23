class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        result = 0 
        
        ROW = len(grid)
        COL = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q.append((row,col))

        while len(q) > 0:
            

            for x in range(len(q)):

                row,col = q.popleft()
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if min(nr,nc) >= 0 and nr < ROW and nc < COL and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            
            if len(q) > 0:
                result += 1

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1

        return result