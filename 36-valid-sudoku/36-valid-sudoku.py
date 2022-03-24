class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        
        def isValid(row,col):
            val = board[row][col]
            for i in range(len(board)):
                if board[i][col] == val and i != row:
                    return False
            for i in range(len(board[0])):
                if board[row][i] == val and i != col:
                    return False
            start_row = (row//3) *3
            start_col = (col//3) *3
            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if board[i][j] == val and (i != row or j != col):
                        return False
            return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if not isValid(i,j):
                    return False
        return True
                    
