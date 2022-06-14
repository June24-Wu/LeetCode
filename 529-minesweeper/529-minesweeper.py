class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board) ; n = len(board[0])
        count = sum(i.count("E") for i in board)
        if count == m * n:
            for i in range(m):
                for j in range(n):
                    board[i][j] = "B"
            return board
        def count(row,col):
            nonlocal m
            nonlocal n
            cnt = 0 ; adjacent = []
            for i , j in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                newRow = row + i ; newCol = col + j
                if 0 <= newRow < m and 0 <= newCol < n:
                    if board[newRow][newCol] == "M":
                        cnt += 1
                    if board[newRow][newCol] == "E":
                        adjacent.append((newRow,newCol))
            return adjacent , cnt
        
        queue = [(click[0],click[1])]
        
        while queue:
            row , col = queue.pop(0)
            if board[row][col] == "M":
                board[row][col] = "X"
                return board
            adjacent , cnt = count(row,col)
            if cnt > 0:
                board[row][col] = str(cnt)
            else:
                board[row][col] = "B"
                queue.extend(adjacent)
        return board
            