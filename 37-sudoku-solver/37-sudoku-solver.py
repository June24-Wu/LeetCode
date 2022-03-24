class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def backtracking():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != ".":
                        continue
                    for val in range(1,10):
                        if isValid(board,i,j,val):
                            board[i][j] = str(val)
                            if backtracking():
                                return True
                            board[i][j] = "."
                    return False
            return True
        
            # for i in range(len(board)): # 遍历行
            #     for j in range(len(board[0])):  # 遍历列
            #         # 若空格内已有数字，跳过
            #         if board[i][j] != '.': continue
            #         for k in range(1, 10):  
            #             if isValid(board,i, j, k):
            #                 board[i][j] = str(k)
            #                 if backtracking(): return True
            #                 board[i][j] = '.'
            #         # 若数字1-9都不能成功填入空格，返回False无解
            #         return False
            return True # 有解
        def isValid(board,row,col,val):
            for i in range(len(board[0])):
                if board[row][i] == str(val):
                    return False
            # 判断同一列是否冲突
            for j in range(len(board)):
                if board[j][col] == str(val):
                    return False
            # 判断同一九宫格是否有冲突
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == str(val):
                        return False
            return True
        backtracking()   