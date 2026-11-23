class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        colSets = defaultdict(set)
        rowSets = defaultdict(set)
        boxSets = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if board[row][col] in colSets[col]:
                    return False
                if board[row][col] in rowSets[row]:
                    return False
                if board[row][col] in boxSets[(row//3,col//3)]:
                    return False

                colSets[col].add(board[row][col])
                rowSets[row].add(board[row][col])
                boxSets[(row//3,col//3)].add(board[row][col])

        return True
