class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        matdict = {}
        m = len(mat) ; n = len(mat[0])
        for i in range(m):
            for j in range(n):
                matdict[mat[i][j]] = [i,j]
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        for idx, i in enumerate(arr):
            row, col = matdict[i]
            rows[row] += 1
            cols[col] += 1
            if rows[row] == n:
                return idx
            if cols[col] == m:
                return idx
        
        