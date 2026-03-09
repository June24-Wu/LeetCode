class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board); n = len(board[0])

        def dfs(r,c):
            if board[r][c] == "X":
                return
            board[r][c] = "S"
            for i, j in [(0,1),(1,0),(-1,0),(0,-1)]:
                newr, newc = r+i, c+j
                if 0 <= newr < m and 0 <= newc < n and board[newr][newc] == "O":
                    dfs(newr,newc)
            return
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
        return
        