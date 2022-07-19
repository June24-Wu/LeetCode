class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = False
        m = len(board)
        n = len(board[0])
        
        def backtracking(row,col,index):
            nonlocal m ; nonlocal n ; nonlocal flag
            if flag == True:
                return
            if index == len(word):
                flag = True
                return
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
                return
            origin = board[row][col]
            board[row][col] = "#"
            for (i,j) in [(1,0),(-1,0),(0,1),(0,-1)]:
                r , c = row + i , col + j
                # if 0 <= r < m and 0 <= c < n:
                backtracking(r,c,index+1)
            board[row][col] = origin
            return
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    backtracking(i,j,0)
        return flag
                
            
        