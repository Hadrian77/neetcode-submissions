class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        cache = {}
        
        def dfs(cache,x,y,board,word,index):

            if index > len(word) - 1:
                return True

            if len(board) <= x or x < 0:
                return False

            if len(board[x]) <= y or y < 0:
                return False
            
            if (x,y) in cache:
                return False
            
            
            
            if board[x][y] != word[index]:
                return False

            #add letter position to cache, check each direction recursively
            cache[(x,y)] = 1

            #if nothing returns true remove letter position from cache and return false
            if dfs(cache,x + 1,y,board,word,index + 1):
                return True
            
            if dfs(cache,x - 1,y,board,word,index + 1):
                return True

            if dfs(cache,x,y + 1,board,word,index + 1):
                return True
            
            if dfs(cache,x,y - 1,board,word,index + 1):
                return True

            cache.pop((x,y))

        
        for x in range(len(board)):
            for y in range(len(board[x])):
                if dfs(cache,x,y,board,word,0):
                    return True

        return False