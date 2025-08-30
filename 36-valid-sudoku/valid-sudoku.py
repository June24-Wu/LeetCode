class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        def is_valid_r(idx):
            a = set()
            for i in range(n):
                if board[idx][i] in a and board[idx][i] != ".":
                    # print("is_valid_r",idx)
                    return False
                a.add(board[idx][i])
            return True
        def is_valid_c(idx):
            a = set()
            for i in range(n):
                # print(idx,a)
                if board[i][idx] in a and board[i][idx] != ".":
                    # print("is_valid_c",idx)
                    return False
                a.add(board[i][idx])
            return True
        def is_valid_sub_box(r,c):
            a = set()
            for i in range(3):
                for j in range(3):
                    if board[r+i][c+j] in a and board[r+i][c+j] != ".":
                        return False
                    a.add(board[r+i][c+j])
            return True
        ans = True
        for i in range(n):
            # print(i,ans)
            ans = ans and is_valid_r(i)
            ans = ans and is_valid_c(i)
            
        for i in range(n // 3):
            for j in range(n // 3):
                ans = ans and is_valid_sub_box(i*3,j*3)
        return ans



        