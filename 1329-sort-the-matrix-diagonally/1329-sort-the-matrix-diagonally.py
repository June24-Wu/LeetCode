class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat) ; n = len(mat[0])
        def func(row,col):
            nonlocal mat ; nonlocal m ; nonlocal n
            point = []
            res = []
            r = row ; c = col
            while r < m and c < n:
                point.append((r,c))
                res.append(mat[r][c])
                r += 1 ; c += 1
            res.sort()
            for idx , (r , c) in enumerate(point):
                mat[r][c] = res[idx]
            return
        for i in range(m):
            func(i,0)
        for i in range(n):
            func(0,i)
        return mat
        