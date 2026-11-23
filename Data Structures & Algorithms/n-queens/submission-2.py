import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        colSet = set()
        posSet = set()  # col + row
        negSet = set()  # col - row
        board = []
        result = []

        for row in range(n):
            board.append([])
            for col in range(n):
                board[row].append(".")

        def backtrack(row, board):
            if row == n:
                result.append(copy.deepcopy(board))
                return
            
            for col in range(n):
                if col not in colSet and col + row not in posSet and col - row not in negSet:
                    colSet.add(col)
                    posSet.add(col + row)
                    negSet.add(col - row)
                    board[row][col] = "Q"
                    backtrack(row + 1, board)
                    colSet.remove(col)
                    posSet.remove(col + row)
                    negSet.remove(col - row)
                    board[row][col] = "."

        backtrack(0,board)

        for board in result:
            for row in range(len(board)):
                board[row] = "".join(board[row])

        return result