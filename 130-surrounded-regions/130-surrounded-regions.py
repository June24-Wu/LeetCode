class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) ; n = len(board[0])
        
        def dfs(row,col):
            if row < 0 or row >= m or col < 0 or col >=n or board[row][col] != "O":
                return
            board[row][col] = "A"
            dfs(row+1,col) ; dfs(row-1,col) ; dfs(row,col+1) ; dfs(row,col-1)
            return
        for i in range(m):
            dfs(i,0) ; dfs(i,n-1)
        for i in range(n):
            dfs(0,i) ; dfs(m-1,i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
                