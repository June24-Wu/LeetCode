class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0 ; m = len(board) ; n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=="X" and (i == 0 or board[i-1][j] != "X") and (j == 0 or board[i][j-1] != "X"):
                    ans+=1
        return ans