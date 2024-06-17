class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img) ; n = len(img[0])
        def get(x,y):
            nonlocal m ; nonlocal n
            if 0 <= x < m and 0 <= y < n:
                return img[x][y] , 1
            else:
                return 0 , 0
        ansli = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = 0 ; cnt = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        ans += get(i+k,j+l)[0]
                        cnt += get(i+k,j+l)[1]
                
                ansli[i][j] = int(ans / cnt)
        return ansli
        