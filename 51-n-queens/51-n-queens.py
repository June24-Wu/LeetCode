class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = [["."]*n for _ in range(n)]
        return_li = []
        
        def isValid(board,row,column):
            for i in range(row):
                if board[i][column] == "Q":
                    return False
            i = row - 1
            j = column - 1
            while i>= 0 and j>=0:
                if board[i][j]== "Q":
                    return False
                i -=1
                j-=1
            i = row-1
            j = column +1
            while i>=0 and j< n:
                if board[i][j]== "Q":
                    return False
                i-=1
                j+=1
            return True
        def get_answer(path):
            new_li = []
            for i in path:
                new_li.append("".join(i))
            return new_li
        def backtracking(start_row):
            if start_row == n:
                return_li.append(get_answer(path[:]))
                return
            for i in range(n):
                if isValid(path,start_row,i):
                    path[start_row][i] = "Q"
                    backtracking(start_row+1)
                    path[start_row][i] = "."
        backtracking(0)
        return return_li
        