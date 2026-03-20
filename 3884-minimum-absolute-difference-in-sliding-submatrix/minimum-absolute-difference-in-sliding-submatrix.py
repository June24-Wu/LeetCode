class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid); n = len(grid[0])

        ans = [[0 for _ in range(n-k+1)] for _ in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                elements = set()
                minval = float("inf")
                for ki in range(k):
                    for kj in range(k):
                        elements.add(grid[i+ki][j+kj])
                elements = list(elements)   
                elements.sort()
                # print(i,j,elements)
                for v in range(1,len(elements)):
                    minval = min(minval,elements[v] - elements[v-1])
                ans[i][j] = minval if minval != float("inf") else 0
        return ans


        