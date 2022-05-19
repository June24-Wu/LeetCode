class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        flag = False
        visited = [[False for _ in range(n)] for i in range(m)]
        def tracking(row,column,start_index):
            # print(board[row][column])
            nonlocal visited
            nonlocal flag
            if flag == True:return
            if visited[row][column] == True:
                return
            if board[row][column] != word[start_index]:
                return
            if start_index == len(word)-1 and board[row][column] == word[start_index]:
                flag = True
                return
            else:
                visited[row][column] = True
                if row + 1 < m:
                    tracking(row+1,column,start_index+1)
                if row - 1 >= 0:
                    tracking(row-1,column,start_index+1)
                if column + 1 < n:
                    tracking(row,column+1,start_index+1)
                if column - 1 >= 0:
                    tracking(row,column-1,start_index+1)
                visited[row][column] = False
        for i in range(m):
            for j in range(n):
                if flag == True:
                    return True
                tracking(i,j,0)
        return flag
                
        
        