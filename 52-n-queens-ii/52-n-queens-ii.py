class Solution:
    def totalNQueens(self, n: int) -> int:
        
        path = [["."]*n for i in range(n)]
        
        def isValid(board,row,col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            i = row - 1 
            j = col - 1
            while i>= 0 and j>= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j-= 1
            i = row - 1
            j = col + 1
            while i>= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -=1
                j+=1
            return True
        
        def backtracking(start_row):
            if start_row == n:
                self.cnt += 1
            for i in range(n):
                if isValid(path,start_row,i):
                    path[start_row][i] = "Q"
                    backtracking(start_row+1)
                    path[start_row][i] = "."
        self.cnt = 0
        backtracking(0)
        return self.cnt